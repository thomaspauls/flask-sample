from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "<h1>Hello world from Kubernetes!</h1><h2>This is a line to test jenkins cicd pipeline</h2>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
