import re
import json
import os
from web.components.driver_browser import Browser
from web.components.web_page import WebPage
from selenium.webdriver.support.ui import Select

class TwiceScheduleCalendar(Browser, WebPage):
    def __init__(self):
        self.initialize_browser()
        self.open_browser()

    def extract_information(self):
        twice_calendar = []

        try:
            years = self.extract_years()
            year_select = Select(years)

            for year_option in year_select.options:
                year = year_option.get_attribute('value')

                year_select.select_by_value(year)
                self.wait_page(1)

                print('year: ',year)
                months = self.extract_months()
                for month in months:
                    month = month.get_attribute('id')
                    self.find(f'#{month}').click()
                    self.wait_page(2)

                    month = month[-2:]
                    days = self.extract_days()

                    for index, day in enumerate(days):
                        day = day.get_attribute('id')
                        day_name = int(day.removeprefix('calendar-weeks-').strip())+1

                        print(f' year: {year}, month: {month}, day: {day_name}')

                        activities = self.extract_activities(day)

                        if len(activities)>0:
                            for activity in activities:
                                if not 'display: none' in activity.get_attribute("style"):
                                    activity = activity.text.strip()
                                    if len(activity)>0:

                                        event = {
                                            "year": year,
                                            "month": month,
                                            "day": day_name,
                                            "event": activity
                                        }
                                        twice_calendar.append(event)

            self.update_json_file(twice_calendar)

        except Exception as e:
            raise Exception(f"Error extracting information: {e}")

    def update_json_file(self, twice_calendar):
        base_path = os.path.dirname(os.path.abspath(__file__))  # Ruta del script actual
        json_path = os.path.join(base_path, 'files', 'twice_calendar.json')

        os.makedirs(os.path.dirname(json_path), exist_ok=True)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(twice_calendar, f, ensure_ascii=False, indent=2)

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
