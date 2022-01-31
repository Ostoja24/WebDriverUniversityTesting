import pytest
from pathlib import Path
from selenium import webdriver

@pytest.fixture(scope="class")
def chrome_setup():
    options = webdriver.ChromeOptions()
    path = Path("C:/TestFiles/chromedriver.exe")
    driver = webdriver.Chrome(executable_path=path, options = options)
    options.add_argument("--no-sandbox")
    options.add_argument("--maximize-window")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def session_browser(chrome_setup):
    yield driver


