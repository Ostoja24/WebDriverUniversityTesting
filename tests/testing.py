import pytest
import pytest_webdriver
from assertpy import assert_that
from page_objects import PageObject, PageElement
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("chrome_setup", "session_browser")
class Testing_class_1():
    # TEST 01 - Title name testing
    def test_01(self, session_browser):
        session_browser.get("https://webdriveruniversity.com/")
        title = session_browser.find_element(By.CSS_SELECTOR, 'a[id="nav-title"]').text()
        assert_that(title).is_equal_to("WebdriverUniversity.com (New Approach To Learning)")

    # TEST 02 - testing contact form
    def test_02(self, session_browser):
        session_browser.driver.get("https://webdriveruniversity.com/")
        form = session_browser.driver.find_element(By.CSS_SELECTOR, "div[h4 = 'Contact Us Form']")
        form.click()
        session_browser.driver.implicitwait(5)
        First_Name = session_browser.driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'First Name']")
        First_Name.send_keys("Łukasz")
        Last_Name = session_browser.driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Last Name']")
        Last_Name.send_keys("0Brzęczyszczykiewicz")
        Email_Address = session_browser.driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Email Address']")
        Email_Address.send_keys("lukas.brz@pl")
        Comments = session_browser.driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Comments']")
        Comments.send_keys("?><:{}!@#$%^*()Ąqś`日漢")
        Submit = session_browser.driver.find_element(By.CSS_SELECTOR, "input[value = 'SUBMIT']")
        Submit.click()
    # TEST 03 - Testing login form
    def test_03(self, session_browser):
        session_browser.get("https://webdriveruniversity.com/Login-Portal/index.html?")
        Login = session_browser.driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Username']")
        Login.send_keys("admin")
        Password = session_browser.driver.find_element(By.CSS_SELECTOR, "input[placeholder = 'Password']")
        Password.send_keys("admin")
        Button = session_browser.driver.find_element(By.CSS_SELECTOR, "button[id = 'login-button']")
        Button.click()
        Text_alert = session_browser.driver.switch_to.alert.text
        assert_that(Text_alert).is_equal_to("validation failed")
    # TEST 04 - file loader
    def test_04(self,session_browser):
        session_browser.get("https://webdriveruniversity.com/File-Upload/index.html")
        Button = session_browser.find_element(By.CSS_SELECTOR, "input[name = 'filename']")
        Button.send_keys("C:\Buggy4.bmp") # HERE YOU SHOULD REPLACE PATH BY RANDOM .BMP FILE FROM YOUR LOCAL DISK
        Submit = session_browser.driver.find_element(By.CSS_SELECTOR,"input[id = 'submit-button']")
        Submit.click()
        Text_alert = session_browser.driver.switch_to.alert.text
        assert_that(Text_alert).is_equal_to("Your file has now been uploaded!")

