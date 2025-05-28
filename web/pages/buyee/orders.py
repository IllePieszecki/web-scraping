from web.components.web_page import WebPage
from selenium.webdriver.common.by import By

class Orders(WebPage):
    def extract_order_detail(self) -> list:
        self.driver.get("https://buyee.jp/mybaggages/shipped/1")
        self.wait_for_element("#luggageInfo_collection")

        first_order = self.find('#luggageInfo_collection li')
        first_order.find_element(By.CSS_SELECTOR, ".g-feather-chevron-up").click()

        order_table = first_order.find_element(By.CSS_SELECTOR, "table.luggageInfo_order")
        products = order_table.find_elements('css selector', 'tbody tr:nth-child(n+2)')
        return products

    def extract_product_info(self):
        products = self.extract_order_detail()

        for product in products:
            columns = product.find_elements(By.TAG_NAME, 'td')
            print(columns)