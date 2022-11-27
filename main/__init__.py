# Import librerias y frameworks
import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from discord.ext import commands

# Inicializo SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    # Configuramos nuestro BOT
    #Configuramos el TOKEN
    app.config['DISCORD_TOKEN'] = os.getenv('DISCORD_TOKEN')
    #Configuramos el prefijo
    bot = commands.Bot(command_prefix=os.getenv('DISCORD_PREFIX'))

    @bot.command(name='sum')
    async def sum(ctx, a: int, b: int):
        response = a + b
        await ctx.send(response)
    bot.run(app.config['DISCORD_TOKEN'])

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
