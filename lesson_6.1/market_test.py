from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.saucedemo.com/')

driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
driver.find_element(By.CSS_SELECTOR, '#login-button').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
driver.find_element(By.CSS_SELECTOR, '#checkout').click()
driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Murad')
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Ninalalov')
driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('363636')
driver.find_element(By.CSS_SELECTOR, '#continue').click()
result = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
driver.quit()


def test_cart_result():
    assert result == 'Total: $58.29'