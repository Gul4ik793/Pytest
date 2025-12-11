import pytest
import time
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("username, password, expected", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("problem_user", "secret_sauce", True),
    ("performance_glitch_user", "secret_sauce", True),
    ("error_user", "secret_sauce", True),
    ("visual_user", "wrong_password", False),
])
def test_login(username, password, expected):
    BASE_URL = 'https://www.saucedemo.com/'
    s = Service(r'./chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.implicitly_wait(5)

    user = driver.find_element(By.ID, 'user-name')
    user.send_keys(username)
    time.sleep(5)
    passw = driver.find_element(By.ID, 'password')
    passw.send_keys(password)
    time.sleep(5)
    butt = driver.find_element(By.ID, 'login-button')
    butt.click()
    if expected:
        assert "inventory.html" in driver.current_url, "Ошибка"
    else:
        assert "inventory.html" not in driver.current_url, "Ошибка"

