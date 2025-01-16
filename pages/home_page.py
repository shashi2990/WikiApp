# pages/home_page.py

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class HomePage(BasePage):

    def scroll_and_click_icons(self):
        """Scroll and click on the icons."""
        self.scroll_down()
        self.click_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/icon'])[2]")
        self.click_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/icon'])[3]")
        self.click_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/icon'])[4]")
        self.click_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='org.wikipedia.alpha:id/icon'])[1]")

    def scroll_back_up(self):
        """Scroll back up."""
        self.scroll_up()
