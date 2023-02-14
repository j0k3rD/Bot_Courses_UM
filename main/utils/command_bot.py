from abc import ABC, abstractmethod
import os, requests
from main.utils.logger import Logger


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
    def __init__(self, logger: Logger):
        self.__api_url = os.getenv('API_URL')
        self.__url = "users"
        self.__user_data = None
        self.__logger = logger

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
        response = requests.post(url = f"{self.__api_url}{self.__url}", json = self.__user_data)
        if response.status_code == 201:
            self.__logger.info(f'User {user_name} created successfully.')
        elif response.status_code == 202:
            self.__logger.warning(f'User {user_name} already exists.')
        elif response.status_code == 404:
            self.__logger.error(f'Error creating user {user_name}.')

class SaveSearchCommand(Command):
    '''
    Clase que implementa el comando para guardar un usuario
    '''
    def __init__(self, logger: Logger):
        self.__api_url = os.getenv('API_URL')
        self.__url = "searches"
        self.__user_data = None
        self.__logger = logger

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
        response = requests.post(url = f"{self.__api_url}{self.__url}", json = self.__user_data)
        if response.status_code == 201:
            self.__logger.info(f'Search {keywords} created successfully.')
        elif response.status_code == 404:
            self.__logger.error(f'Error creating search. User with {discord_id} not found.')


class SaveCourseCommand(Command):
    '''
    Clase que implementa el comando para guardar un usuario
    '''
    def __init__(self, logger: Logger):
        self.__api_url = os.getenv('API_URL')
        self.__url = "courses"
        self.__user_data = None
        self.__logger = logger

    def __set_data(self, discord_id, courses):
        self.__user_data = {
            "courses": courses,
            "discord_id": str(discord_id)
        }

    def execute(self, discord_id, courses):
        '''
        Método para ejecutar el comando.

        args:
            - discord_id: ID del usuario en discord.
            - courses: Lista de cursos.
        '''
        self.__set_data(discord_id, courses)
        response = requests.post(url = f"{self.__api_url}{self.__url}", json = self.__user_data)
        if response.status_code == 201:
            self.__logger.info(f'Courses {courses} created successfully.')
        elif response.status_code == 404:
            self.__logger.error(f'Error creating courses. User with {discord_id} not found.')