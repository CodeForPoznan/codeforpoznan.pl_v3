from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import urandom
import os
from models import db


app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@{hostname}:{port}/{databasename}".format(
    username = os.environ.get('DB_USER'),
    password = os.environ.get('DB_PASSWORD'),
    hostname = os.environ.get('DB_HOST'),
    port = 5432,
    databasename = os.environ.get('DB_NAME'),
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db.app = app
db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    return 'hello cfp!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
