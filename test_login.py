import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")  # Dummy login site
    yield driver
    driver.quit()

def test_valid_login(setup):
    driver = setup
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Logged In Successfully" in driver.page_source

def test_invalid_login(setup):
    driver = setup
    driver.find_element(By.ID, "username").send_keys("invalid")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Your username is invalid!" in driver.page_source

def test_blank_login(setup):
    driver = setup
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Your username is invalid!" in driver.page_source
