from flask import Flask
from flask_cors import CORS

from .config import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

CORS(app)
