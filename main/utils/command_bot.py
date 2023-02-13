from abc import ABC, abstractmethod
import os, requests

class Command(ABC):
    '''
    Clase abstracta que define los métodos que deben implementar las clases que hereden de ella.
    '''

    @abstractmethod
    def execute(self):
        '''
        Método abstracto para ejecutar el comando
        '''
        pass

class SaveUserCommand(Command):
    '''
    Clase que implementa el comando para guardar un usuario
    '''
    def __init__(self):
        self.__api_url = os.getenv('API_URL')
        self.__url = "users"
        self.__user_data = None

    def __set_data(self, discord_id, user_name):
        self.__user_data = {
            "discord_id": discord_id,
            "name": str(user_name)
        }

    def execute(self, discord_id, user_name):
        '''
        Método para ejecutar el comando.

        args:
            - discord_id: ID del usuario en discord.
            - user_name: Nombre del usuario.
        '''
        self.__set_data(discord_id, user_name)
        requests.post(url = f"{self.__api_url}{self.__url}", json = self.__user_data)

class SaveSearchCommand(Command):
    '''
    Clase que implementa el comando para guardar un usuario
    '''
    def __init__(self):
        self.__api_url = os.getenv('API_URL')
        self.__url = "searches"
        self.__user_data = None

    def __set_data(self, discord_id, keywords):
        self.__user_data = {
            "keywords": str(keywords),
            "discord_id": str(discord_id)
        }

    def execute(self, keywords, discord_id):
        '''
        Método para ejecutar el comando.

        args:
            - discord_id: ID del usuario en discord.
            - keywords: Palabra clave para buscar el curso.
        '''
        self.__set_data(discord_id, keywords)
        requests.post(url = f"{self.__api_url}{self.__url}", json = self.__user_data)

class SaveCourseCommand(Command):
    '''
    Clase que implementa el comando para guardar un usuario
    '''
    def __init__(self):
        self.__api_url = os.getenv('API_URL')
        self.__url = "courses"
        self.__user_data = None

    def __set_data(self, discord_id, course):
        self.__user_data = {
            "courses": course,
            "discord_id": str(discord_id)
        }

    def execute(self, discord_id, course):
        '''
        Método para ejecutar el comando.

        args:
            - discord_id: ID del usuario en discord.
            - course: Lista de cursos.
        '''
        self.__set_data(discord_id, course)
        requests.post(url = f"{self.__api_url}{self.__url}", json = self.__user_data)