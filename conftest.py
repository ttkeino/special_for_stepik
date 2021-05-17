import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options


# Добавление нового аргумента language
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language...")


# Установка языка и запуск браузера
@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language:
        print("\nstart chrome browser for test...")
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("language should be")
    yield browser
    print("\nquit browser...")
    browser.quit()
