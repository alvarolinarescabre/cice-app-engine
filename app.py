# CICE Chamo's practice for App Engine
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
       return "Uses like this: App Engine Endpoint + /hello/Chamo"


@app.route('/hello/<name>')
def hello(name):
       return "Hello {}".format(name)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
