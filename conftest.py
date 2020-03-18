import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
