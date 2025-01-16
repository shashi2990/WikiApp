# pages/settings_page.py

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class SettingsPage(BasePage):

    def toggle_switches(self):
        """Toggle switches in settings."""
        self.click_element(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='More options']")
        self.click_element(AppiumBy.XPATH,
                           "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/explore_overflow_settings']")

        # Toggle each switch in the settings
        switches = [
            "(//android.widget.Switch[@resource-id='org.wikipedia.alpha:id/switchWidget'])[1]",
            "(//android.widget.Switch[@resource-id='org.wikipedia.alpha:id/switchWidget'])[2]",
            "(//android.widget.Switch[@resource-id='org.wikipedia.alpha:id/switchWidget'])[3]",
            "(//android.widget.Switch[@resource-id='org.wikipedia.alpha:id/switchWidget'])[4]"
        ]
        for switch in switches:
            self.click_element(AppiumBy.XPATH, switch)
