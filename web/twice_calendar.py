from web.components.driver_browser import Browser
from web.components.web_page import WebPage
import re
from selenium.webdriver.support.ui import Select
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


class TwiceCalendar(Browser, WebPage):
    def __init__(self):
        self.initialize_browser()

    def view_calendar(self):
        twice_calendar = {}

        self.driver.get("https://twicehub.com/twice")
        self.wait_page(3)
        self.find("#mobile").click()
        self.navigate_years(twice_calendar)

        print(json.dumps(twice_calendar, indent=2))

    def navigate_years(self, twice_calendar):
        year_select = self.find('#header_calendar_year')
        year_selector = Select(year_select)

        for year in year_selector.options:
            year = year.get_attribute("value")

            year_selector.select_by_value(year)
            self.wait_page(1)

            twice_calendar[year] = {}

            self.navigate_months(twice_calendar, year)


    def navigate_months(self, twice_calendar, year: str):
        meses = self.find_all('#header_calendar3 table tr td')
        pattern = re.compile(r'^header_calendar_\d{1,2}$')

        for mes in meses:
            if pattern.match(mes.get_attribute("id")):
                month = mes.text
                mes_calendario = f'#{mes.get_attribute("id")}'
                self.find(mes_calendario).click()
                self.wait_page(1)

                twice_calendar[year][month] = {}

                self.navigate_days(twice_calendar, year, month)

    def navigate_days(self, twice_calendar, year: str, month: str):
        calendar_table = self.find('#mobileTable')
        table_elements = calendar_table.find_elements(By.XPATH, "./*")

        for i, linea in enumerate(table_elements):
            print(linea)


    def navigate_days_x(self, twice_calendar, year: str, month: str):
        dias = self.find_all('#mobileTable')
        day_number = 1
        for dia in dias:
            day_events = dia.text
            days = day_events.splitlines()
            for line in days:
                day_number = line.split(" - ")[0] if '-' in days[0] else day_number
                if len(day_number) <= 2:
                    twice_calendar[year][month][day_number] = {}
                else:
                    twice_calendar[year][month][day_number] = line




    def close(self):
        self.driver.quit()


if __name__ == '__main__':
    twice = TwiceCalendar()
    try:
        twice.view_calendar() # ← Acción
    finally:
        twice.close()