from flask import Flask, request, jsonify, session
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from core import BaseConfig

app = Flask(__name__)

app.config.from_object(BaseConfig)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
api = Api(app)

from controllers import *
from models import User, UserRole

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/register', method=['POST'])
def register():
    json_data = request.json