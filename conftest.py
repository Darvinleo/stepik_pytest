import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser', '-B', action='store', default='chrome', help='Choose Browser')
    parser.addoption('--language', '-L', action='store', default='en', help='Preferably language')


@pytest.fixture(scope='function')
def browser(request):
    """Start chosen browser and close after work"""
    options = Options()
    user_language = request.config.getoption('language')
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)
    browser = request.config.getoption('browser')
    if browser == 'chrome':
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(options=options_firefox)
    else:
        raise ValueError(f"Can't open browser with name{browser}, 'chrome' or 'firefox' only available'")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)

    return driver
