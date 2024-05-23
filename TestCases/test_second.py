from selenium.webdriver import Chrome
import time
import pytest
from selenium.webdriver.common.by import By

@pytest.fixture()
def setpath():
    global driver
    driver = Chrome()
    driver.maximize_window()
    yield
    driver.close()

def test_openbrowser(setpath):
    driver.get("https://demoqa.com/text-box")
    driver.execute_script("window.scrollTo(0,2300)")
    driver.find_element(By.ID,"userName").send_keys("Hola mundo")
    time.sleep(3)