<h1 align=center>📚 UM Bot  🤖</h1>

> UM Discord programming course search bot.<br>Repositorio usado para el proyecto Bot Discord de Diseño de Sistemas de la UM 2022.

<h3>Description</h3> 
This Bot is in charge of searching for programming courses on the internet with the help of an App programmed in Python and Flask.
This App is responsible for performing search tasks in browsers such as Chrome or Firefox with the help of Selenium.
It also has a database that registers the users who interact with the bot, the searches that each of these make and saves the courses found in order to show which courses are the most sought after.
<h3>Install</h3>

**Geckodriver:**

- Descargar geckodriver en: [geckodriver-download](https://github.com/mozilla/geckodriver/releases)
- Descomprimir archivo.
- Ejecutar: ```
sudo mv ./geckodriver-v0.31.0-linux64 /usr/bin/geckodriver```
- Dar permisos: ```
sudo chmod +x /usr/bin/geckodriver```

**Requerimientos:**

Utilidades y Frameworks incluidos en los requerimientos:
- Flask
- Flask-Discord
- python-dotenv
- flask_sqalchemy
- selenium
- webdriver-manager

Instrucciones de instalacion:

Ejecutar: ``` 
./install.sh```
