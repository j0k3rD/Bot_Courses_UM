from discord.ext import commands
import os, requests, discord, datetime
from multiprocessing import Process
import ast
from main.constants.bot import BotConstants

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
                embed = self.text_embed_not_found(response, keyword)
            else:
                embed = self.text_embed_found(keyword)
                #Convertir el string en una lista
                x = ast.literal_eval(response.json()['message'])
                # Guardar información del usuario
                user_id = ctx.message.author.id
                user_name = ctx.message.author
                # self.save_user(user_name = user_name, user_id = user_id)

                # Guardar lo escrito por el usuario
                self.save_search(keywords = keyword, user_id = ctx.message.author.id)

                # Guardar los cursos en la base de datos
                self.save_course(courses = x, user_id = user_id)

                self.text_embed_found_setter(ctx, embed, x)
            
            await ctx.send(embed = embed)


        @bot.command(name='top')
        async def top(ctx):
            api_url = os.getenv('API_URL')
            response = requests.get(url=f'{api_url}top/')
            if response.status_code == 404:
                embed = self.text_embed_not_found_top()
            else:
                embed = self.text_embed_found_top()
                #Convertir el string en una lista
                x = ast.literal_eval(response.json()['message'])
                self.text_embed_found_setter(ctx, embed, x)
            
            await ctx.send(embed = embed)

        return Process(target=bot.run, args=(os.getenv('DISCORD_TOKEN'),))

    def save_user(self, user_name, user_id):

        api_url = os.getenv('API_URL')

        # TODO: Comentar el código
        user_data = {
            "discord_id": user_id,
            "name": str(user_name)
        }

        requests.post(url = f"{api_url}users", json = user_data)


    def save_search(self, keywords, user_id):

        api_url = os.getenv('API_URL')

        # # TODO: Comentar el código
        search_data = {
            "keywords": str(keywords),
            "discord_id": str(user_id)
        }

        requests.post(url = f"{api_url}searches", json = search_data)

    def save_course(self, courses, user_id):

        api_url = os.getenv('API_URL')

        # TODO: Comentar el código
        course_data = {
            "courses": courses,
            "discord_id": str(user_id)
        }

        requests.post(url = f"{api_url}courses", json = course_data)


    def text_embed_not_found(self, ctx, user_input):
        embed = discord.Embed(title = f"{BotConstants.BOT_NOT_FIND_COURSE_0} *{user_input}* {BotConstants.BOT_NOT_FIND_COURSE_1}", description = BotConstants.BOT_MORE_COURSE, color = discord.Color.red())
        embed.set_author(name=ctx.message.author)
        embed.set_footer(text=BotConstants.SET_FOOTER)
        embed.timestamp = datetime.datetime.now()
        return embed

    def text_embed_not_found_top(self):
        embed = discord.Embed(title = f"{BotConstants.BOT_TOP_NOT_COURSE}", description = BotConstants.BOT_MORE_COURSE, color = discord.Color.red())
        return embed

    def text_embed_found(self, user_input):
        embed = discord.Embed(title = f"{BotConstants.BOT_FIND_COURSE_0} *{user_input}* {BotConstants.BOT_FIND_COURSE_1}", description = BotConstants.BOT_MORE_COURSE, color = discord.Color.green())
        return embed

    def text_embed_found_top(self):
        embed = discord.Embed(title = f"{BotConstants.BOT_TOP_COURSE}", description = BotConstants.BOT_MORE_COURSE, color = discord.Color.yellow())
        return embed

    def text_embed_found_setter(self, ctx, embed, x):
        if len(x) < 21:
            for i in range(len(x)):
                embed.add_field(name=f"📕 - {x[i][0]}", value=f"{x[i][1]}", inline=False)
            embed.set_author(name=ctx.message.author)
            embed.set_thumbnail(url=BotConstants.THUMBNAIL)
            embed.set_image(url=BotConstants.SET_IMAGE)
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text=BotConstants.SET_FOOTER)
            return embed