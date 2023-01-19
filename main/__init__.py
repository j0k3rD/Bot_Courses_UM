# Import librerias y frameworks
import os, sys
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import discord
from multiprocessing import Process


# Inicializo SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    #Cargo la configuracion de la base de datos
    app.config['API_URL'] = os.getenv('API_URL')

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

    from main.controllers.bot import Bot

    bot = Bot()

    #Usamos multiprocessing para ejecutar el bot y la API
    p1 = bot.bot_up()
    p2 = Process(target=app.run, args=(os.getenv('API_HOST'),os.getenv('API_PORT')))
    p1.start()
    p2.start()
    p1.join()
    p2.join()