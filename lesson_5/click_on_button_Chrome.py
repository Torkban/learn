from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Клик по кнопке
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
for i in range(5):
    driver.find_element(By.XPATH, '//button[contains(text(),"Add Element")]').click()

buttons_del = driver.find_elements(By.CSS_SELECTOR, '.added-manually')
print(len(buttons_del))

 