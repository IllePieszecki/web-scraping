from selenium import webdriver
from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from selenium.webdriver.common.by import By


class Browser:
    def __init__(self):
        self.driver = None

    def initialize_browser(self):
        """Función para inicializar el navegador (driver)"""
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
