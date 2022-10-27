from importsAndConfigs import app
from schemas.matchSchema import MatchSchema
from entities.matchEntity import MatchEntity
from flask import request
from constants import BASE_AUCTION_PRODUCT

db = MatchEntity.prepare_table_match_and_get_db()
with app.app_context():
    db.create_all() #creo todas las tablas (en este caso 1)

match_schema = MatchSchema() #Instanciamos para poder iteractuar con bd para ABM de uno
match_schemas = MatchSchema(many=True) #Para varios/muchos

class IntermediaryMatch():

    def add_new_match():
        data = request.json
        new_match = MatchEntity(data) #creo una instancia
        db.session.add(new_match) #agrego a la bd
        db.session.commit() #termino
        return match_schema.jsonify(new_match)