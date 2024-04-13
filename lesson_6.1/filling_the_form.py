from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

def input_data(s:str):
    """_summary_
Функция для создания ключа и значения для словаря элементов HTML страницы
    Args:
        s (_type_, optional): _description_. Defaults to str.
    """
    return [driver.find_element(By.CSS_SELECTOR, s).get_attribute('name'), driver.find_element(By.CSS_SELECTOR, s)]


selectors_list = ['[name = first-name]','[name = last-name]','[name = address]', '[name = city]','[name = country]', '[name = e-mail]','[name = phone]', '[name = job-position]','[name = company]']
empty_list = ['[name = zip-code]']
test_dict = {}

for i in selectors_list:
    c = list(input_data(i))
    test_dict[c[0]] = c[1]
    
test_dict['first-name'].send_keys('Иван')
test_dict['last-name'].send_keys('Петров')
test_dict['address'].send_keys('Ленина, 55-3')
test_dict['e-mail'].send_keys('test@skypro.com')
test_dict['phone'].send_keys('+7985899998787')
test_dict['city'].send_keys('Москва')
test_dict['country'].send_keys('Россия')
test_dict['job-position'].send_keys('QA')
test_dict['company'].send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, '[type = submit]').click()
good_alerts = driver.find_elements(By.CSS_SELECTOR, '.alert-success')
bad_alerts = driver.find_elements(By.CSS_SELECTOR, '.alert-danger')

good_elems_id = []    
bad_elems_id = []   
for i in good_alerts:
    good_elems_id.append(i.get_attribute('id'))
    
for i in bad_alerts:
    bad_elems_id.append(i.get_attribute('id'))    

driver.quit()