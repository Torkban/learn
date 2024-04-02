from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Клик по кнопке
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
for i in range(5):
    driver.find_element(By.XPATH, '//button[contains(text(),"Add Element")]').click()

buttons_del = driver.find_elements(By.CSS_SELECTOR, '.added-manually')
print(len(buttons_del))
