from selenium.webdriver.common.by import By

from components.driver_browser import Browser
from components.web_page import WebPage
from components.store_page import Stores
from pages.buyee.orders import Orders
from web.pages.buyee.login import Login


class Buyee(Browser, Stores, Login):
    def __init__(self):
        # Inicializa la clase base
        self.initialize_browser()
        self.login()
        self.order = Orders(self.driver)

    def extract_order(self):
        print(self.order.extract_product_info())


    def close(self):
        self.driver.quit()


buyee = Buyee()  # Inicializa Buyee
buyee.extract_order()