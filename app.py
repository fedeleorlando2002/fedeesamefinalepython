from flask import Flask
from flask_pymongo import PyMongo
from flask_smorest import Api
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/libreria'  # Imposta il nome del database come 'libreria'
app.config['API_TITLE'] = 'app_name'
app.config['API_VERSION'] = 'app_version'
app.config['OPENAPI_VERSION'] = '3.0' 
app.config['OPENAPI_URL_PREFIX'] = '/swagger'
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/ui"
app.config['OPENAPI_URL_UI_URL']= 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui-dist/3.24.2/'

with app.app_context():
    app.config['DEFAULT_MONGO_INSTANCE'] = PyMongo(app)
    marshmallow = Marshmallow(app)
    api = Api(app)

    from app_modules.Libri.views import libri_blp
    api.register_blueprint(libri_blp)

    from app_modules.Clienti.views import clienti_blp
    api.register_blueprint(clienti_blp)

    if __name__ == '__main__':
        app.run(debug=True, port=5001)


