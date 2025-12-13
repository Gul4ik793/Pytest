import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys


def test_icon_Input():
    BASE_URL = 'https://demoqa.com/auto-complete'
    s = Service(r'./chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'autoCompleteMultipleInput').send_keys("a")
    driver.implicitly_wait(10)
    options = driver.find_elements(By.CLASS_NAME, "auto-complete__option")
    assert len(options) > 0, "Список вариантов не отображается"
    time.sleep(5)
    driver.quit()


