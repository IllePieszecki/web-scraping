import re

from web.components.driver_browser import Browser
from web.components.web_page import WebPage
from selenium.webdriver.support.ui import Select


class TwiceScheduleCalendar(Browser, WebPage):
    def __init__(self):
        self.initialize_browser()

    def extract_information(self):
        twice_calendar = {}
        self.open_browser()

        years = self.extract_years()
        for year in years.options:
            year = year.get_attribute('value')
            print('>',year)

            months = self.extract_months()
            for month in months:
                month = month.get_attribute('id')

                print('>>',month)

    def open_browser(self):
        self.driver.get("https://twicehub.com/twice")
        self.wait_page(3)
        self.find("#mobile").click()

    def extract_years(self):
        year_selector = self.find('#header_calendar_year')
        year_select = Select(year_selector)

        return year_select

    def extract_months(self):
        months_buttons = self.find_all('#header_calendar3 table tr td')
        pattern = re.compile(r'^header_calendar_\d{1,2}$')
        months = [month for month in months_buttons if pattern.match(month.get_attribute('id'))]

        return months

    def extract_days(self):
        days_list = self.find_all('#mobileTable')


    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    twice = TwiceScheduleCalendar()
    try:
        twice.extract_information()
    finally:
        twice.close()

'''
import json

twice_calendar = {}

year = 2025
month = 10
day = 31
activity = 'TTT Season2'

twice_calendar[year] = {}
twice_calendar[year][month] = {}
twice_calendar[year][month][day] = {"1":"activity"}
twice_calendar[year][month][day] = {"activity"}



print(json.dumps(twice_calendar, indent=2))
'''