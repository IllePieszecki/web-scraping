from selenium import webdriver
from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By


class Browser:
    def __init__(self):
        self.driver = None

    def initialize_browser(self):
        """Función para inicializar el navegador (driver)"""
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
