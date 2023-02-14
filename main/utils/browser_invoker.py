from main.services import FirefoxBrowser, ChromeBrowser
from .invoker import Invoker

class InvokerBrowser(Invoker):
    '''
    Clase creadora de buscadores para scrap_resource.
    '''
    def __init__(self):
        self.__list_commands = {
            'firefox': FirefoxBrowser(),
            'chrome': ChromeBrowser(),
        }

    def get_command(self, command_name):
        command = self.__list_commands.get(command_name)
        if not command:
            raise Exception('Command not found')
        return command
        