from importsAndConfigs import app, auth
from intermediary.intermediaryMatch import IntermediaryMatch
from intermediary.intermediaryUser import IntermediaryUser
from entities.userEntity import UserEntity
from flask import request, g, jsonify, url_for

@auth.verify_password
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

@app.route('/', methods=['GET'])
def hello():
    return "Service (OK)"

@app.route('/add_new_match', methods=['POST'])
def add_new_match():
    return IntermediaryMatch.add_new_match()

@app.route('/register', methods=['POST'])
def register():
    return IntermediaryUser.register()

@app.route('/login')
@auth.login_required
def get_token():
    token = g.user.generate_auth_token(600)
    return jsonify({ 'token': token.decode('ascii'), 'duration': 600 })

@app.route('/dothis', methods=['GET'])
@auth.login_required
def do_this():
    return jsonify({ 'message':'It is done {}'.format(g.user.username) })

if __name__=='__main__':
	app.run(debug=True) 