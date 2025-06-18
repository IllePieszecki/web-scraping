import re
import json
from web.components.driver_browser import Browser
from web.components.web_page import WebPage
from selenium.webdriver.support.ui import Select


class TwiceScheduleCalendar(Browser, WebPage):
    def __init__(self):
        self.initialize_browser()

    def extract_information(self):
        twice_calendar = {}
        self.open_browser()

        try:

            years = self.extract_years()
            year_select = Select(years)

            for year_option in year_select.options:
                year = year_option.get_attribute('value')
                print('>',year)

                year_select.select_by_value(year)
                self.wait_page(2)

                twice_calendar[year] = {}

                months = self.extract_months()
                for month in months:
                    month = month.get_attribute('id')
                    self.find(f'#{month}').click()
                    self.wait_page(2)

                    print('>>',month)
                    twice_calendar[year][month] = {}
                    days = self.extract_days()

                    for index, day in enumerate(days):
                        day = day.get_attribute('id')
                        day_name = int(day.removeprefix('calendar-weeks-').strip())+1

                        twice_calendar[year][month][day_name] = {}

                        activities = self.extract_activities(day)

                        if len(activities)>0:
                            for activity in activities:
                                if not 'display: none' in activity.get_attribute("style"):
                                    activity = activity.text.strip()
                                    if len(activity)>0:
                                        twice_calendar[year][month][day_name][activity] = {}

            with open('web/files/twice_calendar.json', 'w', encoding='utf-8') as f:
                json.dump(twice_calendar, f, ensure_ascii=False, indent=2)

        except Exception as e:
            raise Exception(f"Error extracting information: {e}")

    def open_browser(self):
        self.driver.get("https://twicehub.com/twice")
        self.wait_page(1)

    def extract_years(self):
        year_selector = self.find('#header_calendar_year')
        return year_selector

    def extract_months(self):
        months_buttons = self.find_all('#header_calendar3 table tr td')
        pattern = re.compile(r'^header_calendar_\d{1,2}$')
        months = [month for month in months_buttons if pattern.match(month.get_attribute('id'))]

        return months

    def extract_days(self):
        days_list = self.find_all('#calendar div')
        pattern = re.compile(r'^calendar-weeks-\d{1,2}$')
        weeks = [week for week in days_list if pattern.match(week.get_attribute('id'))]

        return weeks

    def extract_activities(self, element: str):
        activites_list = self.find_all(f'#{element} button')
        return activites_list


    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    twice = TwiceScheduleCalendar()
    try:
        twice.extract_information()
    finally:
        twice.close()

