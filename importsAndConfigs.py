from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from constants import DB_USER, DB_PASSWORD, DATABASE_NAME
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost/{DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #para que no tire errores ni warnings
app.config['SECRET_KEY'] = 'voolkia-prode'    

db = SQLAlchemy(app) #obtenemos una instancia de la bd

ma = Marshmallow()