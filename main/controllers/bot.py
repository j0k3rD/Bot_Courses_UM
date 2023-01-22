from discord.ext import commands
import os, requests, discord
from multiprocessing import Process
import ast


class Bot():

    def bot_up(self):
        discord_intents = discord.Intents.all()
        discord_intents.message_content = True

        bot = commands.Bot(command_prefix=os.getenv('DISCORD_PREFIX'), intents=discord_intents)     
        
        @bot.command(name='search')
        async def search(ctx, keyword: str):
            response = requests.get(f'http://127.0.0.1:5000/api/v1/search/firefox/{keyword}')
            if response.status_code == 404:
                embed = discord.Embed(title = f"No se encontraron cursos sobre *{keyword}*. Por favor, intenta con otra palabra clave.", description = "Para mas Cursos *!search* ;)", color=discord.Color.red())
                embed.set_author(name=ctx.message.author)
                embed.set_footer(text="Cursos de Codigo Facilito")
                embed.timestamp = ctx.message.created_at()
                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(title = f"Encontre unos cursos sobre *{keyword}* para vos! 🤖", description = "Para mas Cursos *!search* ;)", color=discord.Color.yellow())
                #Convertir el string en una lista
                x = ast.literal_eval(response.json()['message'])
                #Mostrar los primeros 3 cursos en diferentes campos
                for i in range(3):
                    embed.add_field(name=f"📕 - {x[i][0]}", value=f"{x[i][1]}", inline=False)
                embed.set_author(name=ctx.message.author)
                # embed.thumbnail(url="https://cdn-icons-png.flaticon.com/512/6008/6008363.png")
                # embed.set_image(url="https://cdn-icons-png.flaticon.com/512/6008/6008363.png")
                embed.timestamp = ctx.message.created_at()
                embed.set_footer(text="Cursos de Codigo Facilito")
                await ctx.send(embed=embed)
        return Process(target=bot.run, args=(os.getenv('DISCORD_TOKEN'),))

    #Agregar para sacar el nombre del usuario


    #Agregar para sacar el # del usuario de ds