from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.market_page import Market_page
import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
m_page = Market_page(driver)
input_dict = {'#user-name':'standard_user','#password':'secret_sauce'}
clc_btns = ['#add-to-cart-sauce-labs-backpack', '#add-to-cart-sauce-labs-bolt-t-shirt','#add-to-cart-sauce-labs-onesie','.shopping_cart_link','#checkout']
post_data = {'#first-name': 'Murad', '#last-name': 'Ninalalov', '#postal-code': '363636'}
m_page.filling_inputs(input_dict)
m_page.clicking_btn('#login-button')
m_page.clickings_btns(clc_btns)
m_page.filling_inputs(post_data)
m_page.clicking_btn('#continue')
result = m_page.get_result()


def test_mrkt():
    assert result == 'Total: $58.29'
    driver.quit()