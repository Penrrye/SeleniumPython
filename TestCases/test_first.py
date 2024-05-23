from selenium.webdriver import Chrome
import time
import pytest

@pytest.fixture()
def setpath():
    global driver
    driver = Chrome()
    driver.maximize_window()
    yield
    driver.close()

def test_openbrowser(setpath):
    driver.get("https://www.google.com/")
    time.sleep(3)