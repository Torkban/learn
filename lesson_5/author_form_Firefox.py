from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Форма авторизации
driver.get('http://the-internet.herokuapp.com/login')
driver.find_element(By.CSS_SELECTOR, '#username').send_keys('tomsmith')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('SuperSecretPassword!')
driver.find_element(By.CSS_SELECTOR, '.radius').click()