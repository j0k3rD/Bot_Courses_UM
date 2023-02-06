from discord.ext import commands
import os, requests, discord, datetime
from multiprocessing import Process
import ast
from main.constants.bot import BotConstants
from main.map import CourseSchema, SearchSchema, UserSchema


class Bot():

    def bot_up(self):
        discord_intents = discord.Intents.all()
        discord_intents.message_content = True

        bot = commands.Bot(command_prefix=os.getenv('DISCORD_PREFIX'), intents=discord_intents)     
        
        @bot.command(name='search')
        async def search(ctx, keyword: str):
            api_url = os.getenv('API_URL')
            response = requests.get(f'{api_url}search/firefox/{keyword}')
            if response.status_code == 404:
                embed = discord.Embed(title = f"{BotConstants.BOT_NOT_FIND_COURSE_0} *{keyword}*. {BotConstants.BOT_NOT_FIND_COURSE_1}", description = BotConstants.BOT_MORE_COURSE, color=discord.Color.red())
                embed.set_author(name=ctx.message.author)
                embed.set_footer(text=BotConstants.SET_FOOTER)
                embed.timestamp = datetime.datetime.now()
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title = f"{BotConstants.BOT_FIND_COURSE_0} *{keyword}* {BotConstants.BOT_FIND_COURSE_1}", description = BotConstants.BOT_MORE_COURSE, color=discord.Color.yellow())
                
                #Convertir el string en una lista
                x = ast.literal_eval(response.json()['message'])

                # Guardar información del usuario
                user_id = ctx.message.author.id
                user_name = ctx.message.author
                self.save_user(user_name = user_name, user_id = user_id)

                # Guardar lo escrito por el usuario
                self.save_search(keywords = keyword, user_id = ctx.message.author.id)

                # Guardar los cursos en la base de datos
                self.save_course(courses = x)

                #Mostrar todos los cursos, pero si son menos de 18, mostrarlos todos
                if len(x) < 21:
                    for i in range(len(x)):
                        embed.add_field(name=f"📕 - {x[i][0]}", value=f"{x[i][1]}", inline=False)
                embed.set_author(name=ctx.message.author)
                embed.set_thumbnail(url=BotConstants.THUMBNAIL)
                embed.set_image(url=BotConstants.SET_IMAGE)
                embed.timestamp = datetime.datetime.now()
                embed.set_footer(text=BotConstants.SET_FOOTER)
                await ctx.send(embed=embed)

        return Process(target=bot.run, args=(os.getenv('DISCORD_TOKEN'),))

    def save_user(self, user_name, user_id):

        api_url = os.getenv('API_URL')

        # TODO: Comentar el código
        user_data = {
            "discord_id": user_id,
            "name": str(user_name)
        }

        r = requests.post(url = f"{api_url}users", json = user_data)

    def save_search(self, keywords, user_id):
        print(f"El usuario con id {user_id}, escribio {keywords}")

    def save_course(self, courses):
        print(f"Los cursos encontrados son: {courses}")