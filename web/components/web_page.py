import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class WebPage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, element: str):
        return self.driver.find_element(By.CSS_SELECTOR, element)

    def find_xpath(self, element: str):
        return self.driver.find_element(By.XPATH, element)

    def find_all(self, element: str, context: WebElement = None):
        if context is None:
            return self.driver.find_elements(By.CSS_SELECTOR, element)
        return context.find_elements(By.CSS_SELECTOR, element)


    def wait_page(self, seconds: int):
        time.sleep(seconds)

    def check_if_exists(self, element: str, timeout=5):
        """
        Validates that the element is visible without performing any
        further actions afterward
        """
        try:
            return (
                WebDriverWait(self.driver, timeout)
                .until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, element)
                    )
                )
                .is_displayed()
            )
        except Exception:
            print(f"ERROR: Element '{element}' not found")
            return False

    def wait_for_element(self, element: str, timeout=10):
        """
        Waits for the element to be located on the page without
        performing any subsequent actions.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, element))
            )
        except:
            print(f"the element '{element}' is not existent yet")

    def scroll_to_element(self, element: str):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)