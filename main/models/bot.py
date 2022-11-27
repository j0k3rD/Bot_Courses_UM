class Bot():
    def __init__(self):
        self.__discord_token = ""
        self.__discord_guild = ""
# 
    @property
    def discord_token(self):
        return self.__discord_token
    @discord_token.setter
    def discord_token(self, discord_token):
        self.__discord_token = discord_token
    @property
    def discord_guild(self):
        return self.__discord_guild
    @discord_guild.setter
    def discord_guild(self, discord_guild):
        self.__discord_guild = discord_guild
    
    def load_env():
        #TODO: cargar variables de entorno referida a discord
        pass
