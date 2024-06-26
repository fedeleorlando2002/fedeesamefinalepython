from marshmallow import fields
from bson import ObjectId
from flask import Flask
from flask_pymongo import PyMongo
from flask_smorest import Api
from flask_marshmallow import Marshmallow, Schema

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/libreria'  # Imposta il nome del database come 'libreria'
app.config['API_TITLE'] = 'app_name'
app.config['API_VERSION'] = 'app_version'
app.config['OPENAPI_VERSION'] = '3.0.0' 
app.config['OPENAPI_URL_PREFIX'] = '/swagger'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/ui'  # Imposta l'endpoint per Swagger UI
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.24.2/'

with app.app_context():
    app.config['DEFAULT_MONGO_INSTANCE'] = PyMongo(app)
    Schema.TYPE_MAPPING[ObjectId] = fields.String
    marshmallow = Marshmallow(app)
    api = Api(app)

    from app_modules.Libri.views import libri_blp
    api.register_blueprint(libri_blp)

    from app_modules.Clienti.views import clienti_blp
    api.register_blueprint(clienti_blp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)