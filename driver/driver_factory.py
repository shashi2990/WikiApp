# driver/driver_factory.py

from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import DEVICE_NAME, PLATFORM_NAME, APP_ACTIVITY, APP_PACKAGE, AUTOMATION_NAME, APPIUM_SERVER_URL

class DriverFactory:
    @staticmethod
    def get_driver():
        """Initialize and return an Appium driver."""
        desired_caps = {
            "deviceName": DEVICE_NAME,
            "platformName": PLATFORM_NAME,
            "appActivity": APP_ACTIVITY,
            "appPackage": APP_PACKAGE,
            "automationName": AUTOMATION_NAME
        }

        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

        # Connect to the Appium server
        driver = webdriver.Remote(APPIUM_SERVER_URL, options=capabilities_options)
        return driver
