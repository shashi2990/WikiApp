# pages/base_page.py

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def click_element(self, by, value):
        """Click on an element."""
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def send_keys(self, by, value, text):
        """Send keys to an element."""
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        element.send_keys(text)

    def get_element(self, by, value):
        """Get an element."""
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def scroll_down(self):
        """Scroll down the screen."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector()).scrollForward()'
        )

    def scroll_up(self):
        """Scroll up the screen."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector()).scrollBackward()'
        )
