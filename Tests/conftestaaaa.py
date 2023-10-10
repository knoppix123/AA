import pytest
from selenium import webdriver
import time
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()


    baseURL = "https://aas.com/"
    driver.get(baseURL)
    driver.maximize_window()
    driver.implicitly_wait(10)




    request.cls.driver = driver
    yield
    driver.quit()

