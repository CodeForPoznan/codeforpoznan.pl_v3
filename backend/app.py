from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import urandom
from models import db

app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@{hostname}:{port}/{databasename}".format(
    username="cfp_v3",
    password="cfp_v3",
    hostname="172.18.0.3",
    port=5432,
    databasename="cfp_v3",
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = urandom(24)

db.app = app
db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    return 'hello cfp!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)




