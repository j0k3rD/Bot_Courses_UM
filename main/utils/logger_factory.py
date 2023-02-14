from .invoker import Invoker
from .logger import ConsoleLogger, FileLogger


class LoggerFactoryImpl(Invoker):
    '''
    Clase que implementa el factory de loggers.
    '''

    def get_command(self, command_name):
        '''
        Método para obtener el logger.
        '''
        dict = {
            'console': ConsoleLogger(),
            'file': FileLogger()
        }
        return dict[command_name]