from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  #Espera a que el HTML deje de cargar para realizar las operaciones
from selenium.webdriver.support import expected_conditions as EC #Para añadir condiciones de busqueda
from selenium.webdriver.common.by import By #Ayuda a configurar esas busquedas
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#import pandas as pd

#User search variable
#to_search = "javascript"

class ScrapServices:

    # def __get_service(self):
    #     return driver_path

    def __get_options(self):
        #Navegation Options
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        options.add_argument('headless');
        options.add_argument('window-size=0x0') ##Comentar para ver como funciona
        return options

    def __get_browser(self):
        # driver_path = "/usr/bin/chromedriver"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.__get_options())
        return driver

    def search(self, keyword:str):
        #Open Browser
        driver=self.__get_browser()
        driver.get(f'https://codigofacilito.com/search?utf8=✓&keyword={keyword}')

        WebDriverWait(driver,5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                            'div.f-card f-padding white'.replace(" ", "."))))\
        .click()

        #Cambiar de pestaña para copiar la URL
        # driver.switch_to.window(driver.window_handles[1])

        url_search = driver.current_url

        print(url_search)

    def save_data(self, data_list):
        pass

    def parser(self):
        pass

# a = ScrapServices()
# a.search("python")