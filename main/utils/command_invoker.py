from .command_bot import SaveCourseCommand, SaveSearchCommand, SaveUserCommand
from .invoker import Invoker
from .logger import Logger

class InvokerCommandsBot(Invoker):
    '''
    Clase creadora de comandos para el bot.
    '''
    def __init__(self, logger: Logger):
        self.__list_commands = {
            'save_user': SaveUserCommand(logger),
            'save_search': SaveSearchCommand(logger),
            'save_course': SaveCourseCommand(logger)
        }

    def get_command(self, command_name):
        command = self.__list_commands.get(command_name)
        if not command:
            raise Exception('Command not found')
        return command
        