# Import librerias y frameworks
import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from discord.ext import commands
import discord
from discord.ext import commands
import requests
from multiprocessing import Process


# Inicializo SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    #Configuramos el TOKEN
    app.config['DISCORD_TOKEN'] = os.getenv('DISCORD_TOKEN')

    #Configuramos el PREFIX
    app.config['DISCORD_PREFIX'] = os.getenv('DISCORD_PREFIX')

    #Configuramos el INTENTS
    app.config['DISCORD_INTENTS'] = discord.Intents.default()
    app.config['DISCORD_INTENTS'].message_content = True

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
    
    #Inicializamos el bot
    bot = commands.Bot(command_prefix=app.config['DISCORD_PREFIX'], intents=app.config['DISCORD_INTENTS'])


    @bot.command(name='search')
    async def search(ctx, keyword: str):
        response = requests.get(f'http://127.0.0.1:5000/api/v1/search/firefox/{keyword}')
        await ctx.send(response.json()['status'])

        
    #Usamos multiprocessing para ejecutar el bot y la API
    p1 = Process(target=bot.run, args=(app.config['DISCORD_TOKEN'],))
    p2 = Process(target=app.run, args=(os.getenv('API_HOST'),os.getenv('API_PORT')))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
