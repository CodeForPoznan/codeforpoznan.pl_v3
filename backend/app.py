from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import urandom
import os
from models import db

from flask_mail import Mail
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

db.app = app
db.init_app(app)


mail = Mail(app)
CORS(app)

if __name__ == '__main__':
    from views import *
    app.run(host='0.0.0.0', debug=True)
