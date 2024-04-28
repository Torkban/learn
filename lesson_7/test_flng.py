from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.filling_page import Filling_page
import pytest


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
f_page = Filling_page(driver)
test_dict = {'[name = first-name]': 'Иван', '[name = last-name]':'Петров', '[name = address]':'Ленина, 55-3', '[name = e-mail]':'test@skypro.com', '[name = phone]': '+7985899998787', '[name = city]':'Москва', '[name = country]':'Россия', '[name = job-position]':'QA', '[name = company]':'SkyPro'}
f_page.filling_inputs(test_dict) 
f_page.clicking_btn('[type = submit]')

def test_green_value(): 
    test_g_list = ['first-name', 'last-name', 'address', 'city', 'country', 'e-mail', 'phone', 'job-position', 'company']
    g_list = f_page.get_green()
    for i in g_list:
        assert i in test_g_list and len(g_list) == 9
        
        
def test_red_value(): 
    test_r_list = ['zip-code']
    r_list = f_page.get_red()
    for i in r_list:
        assert i in test_r_list and len(r_list) == 1
    
    driver.quit()