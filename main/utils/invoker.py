from abc import ABC, abstractmethod

class Invoker(ABC):

    @abstractmethod
    def get_command(self, command_name):
        '''
        Obtener el tipo de comando.

        args:
            - command_name: Nombre del comando.

        return:
            - command: Comando.
        '''
        pass

        