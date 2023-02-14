from abc import ABC
from abc import abstractmethod
from datetime import datetime
import os

class Logger(ABC):
    '''
    Clase abstracta que define los métodos que deben implementar las clases que hereden de ella.
    '''

    @abstractmethod
    def info(self, message):
        '''
        Método abstracto para loguear un mensaje de información.
        '''
        pass

    @abstractmethod
    def error(self, message):
        '''
        Método abstracto para loguear un mensaje de error.
        '''
        pass

    @abstractmethod
    def warning(self, message):
        '''
        Método abstracto para loguear un mensaje de advertencia.
        '''
        pass

    @abstractmethod
    def debug(self, message):
        '''
        Método abstracto para loguear un mensaje de debug.
        '''
        pass


class ConsoleLogger(Logger):
    '''
    Clase que implementa el logger para la consola.
    '''

    def info(self, message):
        '''
        Método para loguear un mensaje de información.

        args:
            - message: Mensaje a loguear.
        '''
        print(f"INFO: {message}")

    def error(self, message):
        '''
        Método para loguear un mensaje de error.

        args:
            - message: Mensaje a loguear.
        '''
        print(f"ERROR: {message}")

    def warning(self, message):
        '''
        Método para loguear un mensaje de advertencia.

        args:
            - message: Mensaje a loguear.
        '''
        print(f"WARNING: {message}")

    def debug(self, message):
        '''
        Método para loguear un mensaje de debug.

        args:
            - message: Mensaje a loguear.
        '''
        print(f"DEBUG: {message}")
    

class FileLogger(Logger):
    '''
    Clase que implementa el logger para un archivo.
    '''

    __new_file = os.getenv('LOG_FILE')

    def __print(self, level, message):
        '''
        Método para loguear un mensaje.

        args:
            - message: Mensaje a loguear.
        '''
        with open(self.__new_file, 'a') as f:
            f.write(f"{datetime.now()} - {level}: {message} \n")
    
    def info(self, message):
        '''
        Método para loguear un mensaje de información.

        args:
            - message: Mensaje a loguear.
        '''
        self.__print(level='INFO', message=message)
    
    def error(self, message):
        '''
        Método para loguear un mensaje de error.

        args:
            - message: Mensaje a loguear.
        '''
        self.__print(level='ERROR', message=message)
    
    def warning(self, message):
        '''
        Método para loguear un mensaje de advertencia.

        args:
            - message: Mensaje a loguear.
        '''
        self.__print(level='WARNING', message=str(message))
    
    def debug(self, message):
        '''
        Método para loguear un mensaje de debug.

        args:
            - message: Mensaje a loguear.
        '''
        self.__print(level='DEBUG', message=message)