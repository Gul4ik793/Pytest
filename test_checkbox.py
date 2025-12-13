import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_icon_check_uncheck():
    BASE_URL = 'https://demoqa.com/checkbox'
    s = Service(r'./chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.implicitly_wait(5)

    driver.find_element(By.XPATH, '//span[text()="Home"]').click()
    time.sleep(2)

    check_icon = driver.find_element(By.CSS_SELECTOR, ".rct-icon.rct-icon-check")
    assert "rct-icon-check" in check_icon.get_attribute("class")

    driver.find_element(By.XPATH, '//span[text()="Home"]').click()
    time.sleep(2)

    check_icon = driver.find_element(By.CSS_SELECTOR, ".rct-icon.rct-icon-uncheck")
    assert "rct-icon rct-icon-uncheck" in check_icon.get_attribute("class")
    time.sleep(2)

    driver.quit()

def test_button():
    BASE_URL = 'https://demoqa.com/checkbox'
    s = Service(r'./chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.implicitly_wait(5)

    driver.find_element(By.CSS_SELECTOR, ".rct-icon.rct-icon-expand-close").click()
    time.sleep(2)

    check_button = driver.find_element(By.CSS_SELECTOR, ".rct-icon.rct-icon-expand-open")
    assert "rct-icon rct-icon-expand-open" in check_button.get_attribute("class")
    assert driver.find_element(By.XPATH, "//span[text()='Desktop']").is_displayed()
    assert driver.find_element(By.XPATH, "//span[text()='Documents']").is_displayed()
    assert driver.find_element(By.XPATH, "//span[text()='Downloads']").is_displayed()

    driver.find_element(By.CSS_SELECTOR, ".rct-icon.rct-icon-expand-open").click()
    time.sleep(2)

    check_button = driver.find_element(By.CSS_SELECTOR, ".rct-icon.rct-icon-expand-close")
    assert "rct-icon rct-icon-expand-close" in check_button.get_attribute("class")

    driver.quit()

