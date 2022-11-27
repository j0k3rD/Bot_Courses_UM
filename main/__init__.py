# Import librerias y frameworks
import os
from flask import Flask
from dotenv import load_dotenv

# Importar SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Inicializo SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    # Si no existe el archivo de base de datos crearlo (para SQLite)
    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Url de configuración de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)
    from main.resources import scrapblue, home 
    app.register_blueprint(home,url_prefix="/api/v1")
    app.register_blueprint(scrapblue,url_prefix="/api/v1")
    return app
