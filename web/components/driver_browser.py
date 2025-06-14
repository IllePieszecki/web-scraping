from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os
load_dotenv()

class Browser():
    def __init__(self):
        self.driver = None


    def initialize_browser(self):
        """Función para inicializar el navegador (driver)"""
        browser = os.environ.get("BROWSER")

        match browser:
            case 'firefox':
                self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
                self.driver.maximize_window()
                self.driver.implicitly_wait(2)
            case "chrome":
                chrome_options = Options()
                chrome_options.add_argument("--headless")  #

                self.driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install())
                    # ,options=chrome_options
                )
                self.driver.maximize_window()
                self.driver.implicitly_wait(2)
            case _:
                raise "A browser wasn't selected"