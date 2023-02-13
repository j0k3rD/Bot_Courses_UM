from .command_bot import SaveCourseCommand, SaveSearchCommand, SaveUserCommand

class Invoker():
    '''
    Clase creadora de comandos para el bot.
    '''
    def __init__(self):
        self.__list_commands = {
            'save_user': SaveUserCommand(),
            'save_search': SaveSearchCommand(),
            'save_course': SaveCourseCommand()
        }

    def get_command(self, command_name):
        '''
        Obtener el tipo de comando.

        args:
            - command_name: Nombre del comando.
            
        return:
            - command: Comando.
        '''
        command = self.__list_commands.get(command_name)
        if not command:
            raise Exception('Command not found')
        return command
        