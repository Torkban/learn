from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 40) 

driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

driver.find_element(By.CSS_SELECTOR, '#delay').clear()
driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')
driver.find_element(By.XPATH, '//span[contains(text(), "7")]').click()
driver.find_element(By.XPATH, '//span[contains(text(), "+")]').click()
driver.find_element(By.XPATH, '//span[contains(text(), "8")]').click()
driver.find_element(By.XPATH, '//span[contains(text(), "=")]').click()

waiter.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[style = "display: none;"]'))
)


result = driver.find_element(By.CSS_SELECTOR, '.screen').text

def test_checking_result():
    assert result == '15'
    
driver.quit()
