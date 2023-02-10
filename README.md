<h1 align=center>📚 UM Bot  🤖</h1>

> UM Discord programming course search bot.<br>Repositorio usado para el proyecto Bot Discord de Diseño de Sistemas de la UM 2022.

<h3>Description</h3> 
This Bot is a solution to search for programming courses on the internet. The application, programmed in Python and Flask, uses Selenium to perform searches in browsers such as Chrome or Firefox. In addition, it has an SQL database that records user interactions with the Bot, including the searches performed and the courses found. This way, you can determine which courses are the most popular and offer personalized suggestions to users in the future.

<h3>Install</h3>

- 1 - Download or clone the repository to your local environment.
- 2 - **Geckodriver:**
  - Download geckodriver at: [geckodriver-download](https://github.com/mozilla/geckodriver/releases)
  - Unzip the file.
  - Execute: ```
  sudo mv ./geckodriver-v0.31.0-linux64 /usr/bin/geckodriver```
  - Give permissions: ```
  sudo chmod +x /usr/bin/geckodriver```
- 4 - Create a Discord Bot: [Create-Discord-App](https://discord.com/developers/applications)
  - Go to *Bot* and create new. (IMPORTANT: If the name of the application is already in use, you will have to change it to be able to create the bot.)
  - Go to the bot repository and create a new ".env" file with the format you found in the ".env-example" file.
  - Replace:
    - 'DATABASE_PATH': with the location of the repository on your pc. Example: "/home/user/Desktop/Bot_Courses_UM"
    - 'DISCORD_PREFIX': whatever prefix you want to use on Discord to communicate with the bot. Example: "!"
    - 'DISCORD_TOKEN': From the 'discord developers' page where you created the bot, copy your bot token. (IMPORTANT: do not share this token)
    - Save the changes made.
- Now on the 'discord developers' page, go to 'OAuth2' -> 'URL Generator' under 'Scopes' choose 'Bot' and under 'Bot Permissions' choose 'Administrator'.
Once this is done, copy the invitation link that will be generated at the bottom.
- Paste it into your browser and then choose the server you want to invite the bot to and click 'Continue'.
- 3 - Execute: ```
  sh install.sh```
- 4 - Execute: ```
  sh boot.sh```

<h3>How to Use</h3>
Usage is the same as any Discord Bot. Once the prefix for the bot has been set, we will have two commands to use. (Example assuming I don't change the default prefix which is '!')

- **"!search"**: This command, followed by the course keyword you want to search for. Example: if I want to search for courses on "c++", I will have to write "!search c++". And the bot will perform the search and return a list of courses on that specific topic.

- **"!top"**: This command will show us on the screen a list with the 10 most searched courses by the bot. (In the event that it is your own bot and it is not "CoursesUMBot", you will have to perform several searches for this ranking to be generated)."

<h3>Documentation</h3>

Please see the [**online documentation**](https://github.com/j0k3rD/Bot_Courses_UM/wiki) for more information on how to use this Bot.

<h3>Contribution</h3>
If you want to contribute to this project, please follow the steps below:

1. Fork the repository.
2. Make your changes in a separate branch.
3. Make a pull request with your changes.

<h3>Author</h3>

This project was created by [**XxRaXoRxX**](https://github.com/XxRaXoRxX) and [**j0k3rD**](https://github.com/j0k3rD).

<h3>Thanks</h3>

We thank everyone who has contributed to this project and supported it in any way. Thank you for your cooperation!
