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
- 3 - Execute: ```
  sh install.sh```
- 4 - Execute: ```
  sh boot.sh```
  
**Requirements:**

Utilities and Frameworks included in the requirements:
- Flask
- Flask-Discord
- python-dotenv
- flask_sqalchemy
- selenium
- webdriver-manager
