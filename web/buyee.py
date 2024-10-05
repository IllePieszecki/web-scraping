from selenium import webdriver
from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from selenium.webdriver.common.by import By
from components.web_page import WebPage
from components.driver_browser import Browser
import os
from dotenv import load_dotenv


class Buyee(WebPage, Browser):
    def __init__(self):
        # Inicializa la clase base
        self.initialize_browser()
        WebPage.__init__(self, self.driver)
        load_dotenv()

    def login(self):
        self.driver.get("https://buyee.jp/")
        self.wait_page(2)
        if self.check_if_exists(".g-modalBanner__closeButton.blue"):
            self.find(".g-modalBanner__closeButton.blue").click()
        self.find("a.button.link").click()

        self.find("#login_mailAddress").send_keys(os.getenv('BUYEE_USER'))
        self.find("#login_password").send_keys(os.getenv('BUYEE_PASSWD'))
        self.find(".btn_signup_blue").click()

        self.wait_page(2)

        self.driver.get("https://buyee.jp/mybaggages/shipped/1")
        self.wait_for_element("#luggageInfo_collection")

        first_order = self.find('#luggageInfo_collection li')
        first_order.find_element(By.CSS_SELECTOR,".g-feather-chevron-up").click()

        order_table = first_order.find_element(By.CSS_SELECTOR, "table.luggageInfo_order")
        products = order_table.find_elements('css selector', 'tbody tr:nth-child(n+2)')
        print(len(products))

        for product in products:
            columns = product.find_elements(By.TAG_NAME, 'td')
            row_data = [col.text for col in columns]
            page_origin = row_data[0]
            link = columns[2].find_element(By.TAG_NAME, 'a').get_attribute('href')
            print(link)


        self.close()

    def close(self):
        self.driver.quit()


buyee = Buyee()  # Inicializa Buyee
buyee.login()
