from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/libreria'
    mongo.init_app(app)

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app

