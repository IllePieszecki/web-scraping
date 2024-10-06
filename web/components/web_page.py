import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WebPage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, element: str):
        return self.driver.find_element(By.CSS_SELECTOR, element)

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


