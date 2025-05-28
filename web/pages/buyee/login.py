import os

from dotenv import load_dotenv
from web.components.web_page import WebPage

class Login(WebPage):
    def login(self):
        load_dotenv()

        self.driver.get("https://buyee.jp/")
        self.wait_page(2)
        if self.check_if_exists(".g-modalBanner__closeButton.blue"):
            self.find(".g-modalBanner__closeButton.blue").click()
        self.find("a.button.link").click()

        self.find("#login_mailAddress").send_keys(os.getenv('BUYEE_USER'))
        self.find("#login_password").send_keys(os.getenv('BUYEE_PASSWD'))
        self.find(".btn_signup_blue").click()
