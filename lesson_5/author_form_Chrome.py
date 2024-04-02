from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Форма авторизации
driver.get('http://the-internet.herokuapp.com/login')
driver.find_element(By.CSS_SELECTOR, '#username').send_keys('tomsmith')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('SuperSecretPassword!')
driver.find_element(By.CSS_SELECTOR, '.radius').click()