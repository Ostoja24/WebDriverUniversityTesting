import pytest
from pathlib import Path
from selenium import webdriver
# FIXTURE WITH SETUP WEBDRIVER
@pytest.fixture(scope="class")
def chrome_setup():
    options = webdriver.ChromeOptions()
    path = Path("C:/TestFiles/chromedriver.exe") # PLEASE REPLACE HERE YOUR PATH TO DRIVER ON LOCAL DISK
    driver = webdriver.Chrome(executable_path=path, options = options)
    options.add_argument("--no-sandbox")
    options.add_argument("--maximize-window")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def session_browser(chrome_setup):
    yield driver


