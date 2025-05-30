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
        self.navigate_years(twice_calendar,'2015')

        print(json.dumps(twice_calendar, indent=2))

    def navigate_years(self, twice_calendar, year_selected: str = ""):
        year_select = self.find('#header_calendar_year')
        year_selector = Select(year_select)

        if year_selected == "":
            for year in year_selector.options:
                year = year.get_attribute("value")

                year_selector.select_by_value(year)
                self.wait_page(1)

                twice_calendar[year] = {}

                self.navigate_months(twice_calendar, year)
        else:
            year_selector.select_by_value(year_selected)
            self.wait_page(1)

            twice_calendar[year_selected] = {}

            self.navigate_months(twice_calendar, year_selected)


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

    def fill_days(self, month_activities: str, calendar_table, year: str, month: str):
        days_string = month_activities.splitlines()
        i_dia = 1

        clean_days = list(filter(lambda x: x != "", days_string))
        clean_days = list(filter(lambda x: x and x.strip(), clean_days))

        for i, linea in enumerate(clean_days):
            if '-' in linea:
                i_dia = i
            if i > i_dia:

                if '[' in linea:
                    linea_2 = re.split(r'(?=\[\d{2}:\d{2}\])', linea)
                    linea_2 = list(filter(lambda x: x and x.strip(), linea_2))

                    linea_2 = [f'{x.strip()}' if x.strip().startswith('[') else f'[{x.strip()}' for x in linea_2]

                    if len(linea_2) > 1:
                        calendar_table[year][month][i] = linea_2
                    else:
                        calendar_table[year][month][i] = linea_2[0]
                else:
                    calendar_table[year][month][i] = linea.strip()



    def navigate_days(self, twice_calendar, year: str, month: str):
        calendar_table = self.find_all('#mobileTable')

        self.fill_days(calendar_table[0].text, twice_calendar, year, month)

    def close(self):
        self.driver.quit()


if __name__ == '__main__':
    twice = TwiceCalendar()
    try:
        twice.view_calendar() # ← Acción
    finally:
        twice.close()