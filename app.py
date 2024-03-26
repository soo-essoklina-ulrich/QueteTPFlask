from flask import Flask
from flask_cors import CORS
from extensions import db

from charity import charity_web, charity_api

app = Flask(__name__)
app.register_blueprint(charity_web, url_prefix='/charity-web')
app.register_blueprint(charity_api, url_prefix='/charity-api')
CORS(app, origins="*")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456789@localhost:3306/charity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='', port=8081)
