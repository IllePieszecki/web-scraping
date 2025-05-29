from web.components.driver_browser import Browser
from web.components.web_page import WebPage
import re
from selenium.webdriver.support.ui import Select


class TwiceCalendar(Browser, WebPage):
    def __init__(self):
        self.initialize_browser()

    def view_calendar(self):
        self.driver.get("https://twicehub.com/twice")
        self.wait_page(3)
        self.find("#mobile").click()
        self.navigate_years()

    def navigate_years(self):
        year_select = self.find('#header_calendar_year')
        year_selector = Select(year_select)

        for year in year_selector.options:
            year = year.get_attribute("value")

            year_selector.select_by_value(year)
            self.wait_page(1)

    def navigate_months(self):
        meses = self.find_all('#header_calendar3 table tr td')
        pattern = re.compile(r'^header_calendar_\d{1,2}$')

        for mes in meses:
            if pattern.match(mes.get_attribute("id")):
                mes_calendario = f'#{mes.get_attribute("id")}'
                self.find(mes_calendario).click()
                self.wait_page(1)


    def navigate_days(self):
        dias = self.find_all('#mobileTable')
        for dia in dias:
            print(dia.text)

    def close(self):
        self.driver.quit()

twice = TwiceCalendar()
try:
    twice.view_calendar() # ← Acción
finally:
    twice.close()