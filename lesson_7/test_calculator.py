from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import Calculator_page
import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_page = Calculator_page(driver)
c_page.prep()
btns_list = ['//span[contains(text(), "7")]', '//span[contains(text(), "+")]', '//span[contains(text(), "8")]','//span[contains(text(), "=")]']
c_page.btns_clickng(btns_list)
result = c_page.get_result()
    
def test_calc():
    assert result == '15'
    
    driver.quit()
