from web.components.driver_browser import Browser
from web.components.web_page import WebPage


class TwiceCalendar(Browser, WebPage):
    def __init__(self):
        self.initialize_browser()

    def view_calendar(self):
        self.driver.get("https://twicehub.com/twice")
        self.wait_page(3)

    def close(self):
        self.driver.quit()

twice = TwiceCalendar()
try:
    twice.view_calendar() # ← Acción
finally:
    twice.close()