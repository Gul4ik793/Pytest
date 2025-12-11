import pytest
from saucedemo import login
import time
from quopri import ESCAPE
from re import search

from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



@pytest.mark.parametrize("Username", "password", "expected", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", True),
    ("problem_user", "secret_sauce", True),
    ("performance_glitch_user", "secret_sauce", True),
    ("error_user", "secret_sauce", True),
    ("visual_user", "secret_sauce", True),
])
def test_login(username, password, expected):
    BASE_URL = 'https://www.saucedemo.com/'
    s = Service(r'./chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.implicitly_wait(5)
    user = driver.find_element(By.ID, 'user-name')
    user.send_keys("standard_user")
    time.sleep(5)
    passw = driver.find_element(By.ID, 'password')
    passw.send_keys("secret_sauce")
    time.sleep(5)
    butt = driver.find_element(By.ID, 'login-button')
    butt.click()
    assert url == 'https://www.saucedemo.com/inventory.html/', "Ошибка"

