from discord.ext import commands
import os, requests, discord
from multiprocessing import Process

class Bot():

    def bot_up(self):
        discord_intents = discord.Intents.default()
        discord_intents.message_content = True

        bot = commands.Bot(command_prefix=os.getenv('DISCORD_PREFIX'), intents=discord_intents)     

        @bot.command(name='search')
        async def search(ctx, keyword: str):
            response = requests.get(f'http://127.0.0.1:5000/api/v1/search/firefox/{keyword}')
            await ctx.send(response.json()['message'])

        return Process(target=bot.run, args=(os.getenv('DISCORD_TOKEN'),))

    #Agregar para sacar el nombre del usuario


    #Agregar para sacar el # del usuario de ds