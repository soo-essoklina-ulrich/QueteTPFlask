from flask import Flask, jsonify
from flask_cors import CORS
from quete import quete_bp

app = Flask(__name__, static_folder='quete/static', template_folder='quete/templates')
app.register_blueprint(quete_bp, url_prefix='')

CORS(app, origins="*")


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True, host='', port=8081)
