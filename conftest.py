import pytest
from selene import browser


@pytest.fixture
def browser_driver():
    browser.config.driver_name = 'firefox'
    browser.config.window_width = 1200
    browser.config.window_heigh = 800
    browser.open('https://google.com/ncr')
    yield browser
    browser.quit()
