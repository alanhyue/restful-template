from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import config

db = SQLAlchemy()
cors = CORS()

def create_app(configname):
    app = Flask(__name__, 
            static_folder = config['default'].FLASK_STATIC_FOLDER,
            template_folder = config['default'].FLASK_TEMPLATE_FOLDER)
    app.config.from_object(config.get(configname) or config['default'])

    db.init_app(app)
    cors.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint, url_prefix=None)

    return app
