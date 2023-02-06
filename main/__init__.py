# Import librerias y frameworks
import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from multiprocessing import Process

# Inicializo Api
api = Api()

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

    # Registro los blueprints
    from main.resources import scrapblue, home 
    app.register_blueprint(home,url_prefix="/api/v1")
    app.register_blueprint(scrapblue,url_prefix="/api/v1")

    # Importo los controladores
    import main.controllers as controllers
    from main.controllers.bot import Bot

    api.add_resource(controllers.UserController, '/api/v1/user/<int:id>')
    api.add_resource(controllers.UsersController, '/api/v1/users')
    api.add_resource(controllers.CourseController, '/api/v1/course/<int:id>')
    api.add_resource(controllers.CoursesController, '/api/v1/courses')
    api.add_resource(controllers.SearchController, '/api/v1/search/<int:id>')
    api.add_resource(controllers.SearchesController, '/api/v1/searches')
    api.init_app(app)

    bot = Bot()

    #Usamos multiprocessing para ejecutar el bot y la API
    p1 = bot.bot_up()
    p2 = Process(target=app.run, args=(os.getenv('API_HOST'),os.getenv('API_PORT')))
    p1.start()
    p2.start()
    p1.join()
    p2.join()