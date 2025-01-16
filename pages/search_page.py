# pages/search_page.py

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class SearchPage(BasePage):

    def search_for_text(self, text):
        """Search for a given text."""
        self.click_element(AppiumBy.XPATH,
                           "//android.widget.AutoCompleteTextView[@resource-id='org.wikipedia.alpha:id/search_src_text']")
        self.send_keys(AppiumBy.XPATH,
                       "//android.widget.AutoCompleteTextView[@resource-id='org.wikipedia.alpha:id/search_src_text']",
                       text)

    def clear_search(self):
        """Clear the search query."""
        self.click_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Clear query']")
