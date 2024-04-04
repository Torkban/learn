from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Клик по кнопке без ID
driver.get('http://uitestingplayground.com/dynamicid')
driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
