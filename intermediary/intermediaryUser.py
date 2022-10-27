from importsAndConfigs import app
from schemas.userSchema import UserSchema
from entities.userEntity import UserEntity
from flask import request, g, abort, jsonify

db = UserEntity.prepare_table_user_and_get_db()
with app.app_context():
    db.create_all() #creo todas las tablas (en este caso 1)

match_schema = UserSchema() #Instanciamos para poder iteractuar con bd para ABM de uno
match_schemas = UserSchema(many=True) #Para varios/muchos

class IntermediaryUser():
    def verify_password(username_or_token, password):
        # first try token
        user = UserEntity.verify_auth_token(username_or_token)
        # then check for username and password pair
        if not user:
            user = UserEntity.query.filter_by(username = username_or_token).first()
            if not user or not user.verify_password(password):
                return False
        g.user = user
        return True

    def register():
        username = request.json.get('username') 
        password = request.json.get('password')
        # Check for blank requests
        if username is None or password is None:
            abort(400)
        # Check for existing users
        if UserEntity.query.filter_by(username = username).first() is not None:
            abort(400)
        user = UserEntity(username = username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return (jsonify({'username': user.username}), 201)

    def get_token():
        token = g.user.generate_auth_token(600)
        return jsonify({ 'token': token.decode('ascii'), 'duration': 600 })

    def do_this():
        return jsonify({ 'message':'It is done {}'.format(g.user.username) })