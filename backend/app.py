from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'hello cfp!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
