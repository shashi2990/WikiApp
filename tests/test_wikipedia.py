# tests/test_wikipedia.py

import time
import pytest
from driver.appium_server import start_appium_server, stop_appium_server
from driver.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.settings_page import SettingsPage


@pytest.fixture(scope="function")
def setup():
    """Start Appium server and driver."""
    appium_server = start_appium_server()
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()
    stop_appium_server(appium_server)


def test_home_page_navigation(setup):
    driver = setup
    home_page = HomePage(driver)

    home_page.scroll_and_click_icons()
    time.sleep(5)
    home_page.scroll_back_up()
    time.sleep(2)


def test_search_functionality(setup):
    driver = setup
    search_page = SearchPage(driver)

    search_page.search_for_text("New York")
    time.sleep(5)
    search_page.clear_search()
    time.sleep(2)


def test_settings_toggle(setup):
    driver = setup
    settings_page = SettingsPage(driver)

    settings_page.toggle_switches()
    time.sleep(5)
