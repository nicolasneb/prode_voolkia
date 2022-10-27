from importsAndConfigs import db

class MatchEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer)
    stage = db.Column(db.String(255))
    match_prediction = db.Column(db.String(255))

    def __init__(self, data): #constructor, se ejecuta cada vez que se instancia la clase
        self.id_user = data['id_user']
        self.stage = data['stage']
        self.match_prediction = data['match_prediction']

    def prepare_table_match_and_get_db():
        return db