from discord.ext import commands
import os, requests, discord, datetime
from multiprocessing import Process
import ast
from main.constants.controllers import BotConstants
from main.utils.command_invoker import Invoker
from main.utils.logger import Logger


class Bot():
    '''
    Clase que crea el bot de discord.

    args:
        - invoker: Objeto que invoca los comandos del bot.
        - logger: Objeto que loguea los mensajes.
    '''
    def __init__(self, invoker: Invoker, logger: Logger):
        self.__invoker = invoker
        self.__logger = logger

    def bot_up(self):
        '''
        Función que levanta el bot de discord.

        return:
            - Process: Devuelve el proceso con la función del bot y el token.
        '''

        discord_intents = discord.Intents.all()
        discord_intents.message_content = True

        bot = commands.Bot(command_prefix=os.getenv('DISCORD_PREFIX'), intents=discord_intents)     

        @bot.command(name='search')
        async def search(ctx, keyword: str):
            '''
            Función que busca un curso en la API, se lo envia la cliente y lo guarda en la base de datos.

            args:
                - ctx: Contexto del mensaje.
                - keyword: Palabra clave para buscar el curso.
            '''
            api_url = os.getenv('API_URL')
            self.__logger.bot(f'User {ctx.message.author} is searching for {keyword}')
            response = requests.get(f'{api_url}search/{BotConstants.BROWSER_TYPE}/{keyword}')
            
            if (self.__invoker != None):
                # Guardar usuario
                save_user = self.__invoker.get_command('save_user')
                save_search = self.__invoker.get_command('save_search')
                save_course = self.__invoker.get_command('save_course')
            else:
                self.__logger.error("Invoker is Null")
                print("Invoker is Null")
                return

            # Guardar información del usuario
            user_name = ctx.message.author
            user_id = ctx.message.author.id

            if response.status_code == 404:
                self.__logger.bot(f'Course {keyword} not found.')
                save_user.execute(user_name = user_name, discord_id = user_id)
                save_search.execute(keywords = keyword, discord_id = user_id)
                embed = self.__text_embed_not_found(ctx, keyword)
            else:
                self.__logger.bot(f'Course {keyword} found.')
                embed = self.__text_embed_found(keyword)
                #Convertir el string en una lista
                courses = ast.literal_eval(response.json()['message'])

                save_user.execute(user_name = user_name, discord_id = user_id)
                # Guardar lo escrito por el usuario
                save_search.execute(keywords = keyword, discord_id = user_id)
                # Guardar los cursos en la base de datos
                save_course.execute(courses = courses, discord_id = user_id)

                self.__text_embed_found_setter(ctx, embed, courses)

            self.__logger.bot(f'Course {keyword} sent to {ctx.message.author}')
            
            await ctx.send(embed = embed)

        @bot.command(name='top')
        async def top(ctx):
            '''
            Función que busca los cursos más populares en la API y los envia a la cliente.

            args:
                - ctx: Contexto del mensaje.
            '''
            api_url = os.getenv('API_URL')
            response = requests.get(url=f'{api_url}top/')
            if response.status_code == 404:
                embed = self.__text_embed_not_found_top()
            else:
                embed = self.__text_embed_found_top()
                #Convertir el string en una lista
                courses = ast.literal_eval(response.json()['message'])
                self.__text_embed_found_setter(ctx, embed, courses)
            
            await ctx.send(embed = embed)

        return Process(target=bot.run, args=(os.getenv('DISCORD_TOKEN'),))

    def __text_embed_not_found(self, ctx, user_input):
        '''
        Función que crea el embed de no encontrado para el comando search.

        args:
            - ctx: Contexto del mensaje.
            - user_input: Palabra clave para buscar el curso.
        return:
            - embed: Devuelve mensaje personalizado para discord.
        '''
        embed = discord.Embed(title = f"{BotConstants.BOT_NOT_FIND_COURSE_0} *{user_input}* {BotConstants.BOT_NOT_FIND_COURSE_1}", description = BotConstants.BOT_MORE_COURSE, color = discord.Color.red())
        embed.set_author(name=ctx.message.author)
        embed.set_footer(text=BotConstants.SET_FOOTER)
        embed.timestamp = datetime.datetime.now()
        return embed


    def __text_embed_not_found_top(self):
        '''
        Función que crea el embed de no encontrado para el comando top.

        return:
            - embed: Devuelve mensaje personalizado para discord.
        '''
        embed = discord.Embed(title = f"{BotConstants.BOT_TOP_NOT_COURSE}", description = BotConstants.BOT_MORE_COURSE, color = discord.Color.red())
        return embed


    def __text_embed_found(self, user_input):
        '''
        Función que crea el embed de encontrado para el comando search.

        args:
            - user_input: Palabra clave para buscar el curso.
        return:
            - embed: Devuelve mensaje personalizado para discord.
        '''
        embed = discord.Embed(title = f"{BotConstants.BOT_FIND_COURSE_0} *{user_input}* {BotConstants.BOT_FIND_COURSE_1}", description = BotConstants.BOT_MORE_COURSE, color = discord.Color.green())
        return embed


    def __text_embed_found_top(self):
        '''
        Función que crea el embed de encontrado para el comando top.
        
        return:
            - embed: Devuelve mensaje personalizado para discord.
        '''
        embed = discord.Embed(title = f"{BotConstants.BOT_TOP_COURSE}", description = BotConstants.BOT_MORE_COURSE, color = discord.Color.yellow())
        return embed


    def __text_embed_found_setter(self, ctx, embed, courses):
        '''
        Función que customiza el embed de encontrado para el comando search y top.

        args:
            - ctx: Contexto del mensaje.
            - embed: Embed a customizar.
            - cursos: Lista de cursos.
        '''
        if len(courses) < 21:
            for i in range(len(courses)):
                embed.add_field(name=f"📕 - {courses[i][0]}", value=f"{courses[i][1]}", inline=False)
            embed.set_author(name=ctx.message.author)
            embed.set_thumbnail(url=BotConstants.THUMBNAIL)
            embed.set_image(url=BotConstants.SET_IMAGE)
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text=BotConstants.SET_FOOTER)
            return embed