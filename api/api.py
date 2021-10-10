
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS
app = Flask(__name__)
api = Api(app)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()


import models, resources

api.add_resource(resources.ESDL, '/esdls')
api.add_resource(resources.IdESDL, '/esdls/<int:id>')
api.add_resource(resources.Published,"/esdls/published")
