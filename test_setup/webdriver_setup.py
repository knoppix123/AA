from selenium.webdriver.common.by import By
import time
import os

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def se(request):


    # driver = webdriver.Chrome()
    driver = webdriver.Chrome()

    driver.maximize_window()
    baseurl = "https://skiplagged.com/"
    driver.get(baseurl)
    driver.implicitly_wait(5)

    # Replace time.sleep() with an explicit wait

    yield driver
    driver.quit()

