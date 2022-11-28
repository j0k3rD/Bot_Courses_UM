import os, discord

class Bot():
    def __init__(self):
        self.__discord_token = os.getenv('DISCORD_TOKEN')
        # self.__discord_guild = ""
        self.__discord_prefix = os.getenv('DISCORD_PREFIX')
        self.__discord_intents = discord.Intents.default()
        self.__discord_intents.message_content = True


    @property
    def discord_token(self):
        return self.__discord_token
    # @property
    # def discord_guild(self):
    #     return self.__discord_guild
    # @discord_guild.setter
    # def discord_guild(self, discord_guild):
    #     self.__discord_guild = discord_guild
    
    @property
    def discord_prefix(self):
        return self.__discord_prefix
    
    @property
    def discord_intents(self):
        return self.__discord_intents

    
    def load_env():
        #TODO: cargar variables de entorno referida a discord
        pass