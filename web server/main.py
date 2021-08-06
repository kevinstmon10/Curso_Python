from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    return "<div>Hola</div>"


if __name__ == '__main__':
    app.run(debug=True)
