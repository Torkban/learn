from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Модальное окно

driver.get('http://the-internet.herokuapp.com/entry_ad')
sleep(3)
driver.find_element(By.CSS_SELECTOR, '.modal-footer').click()

    