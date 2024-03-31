from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Клик по кнопке
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
for i in range(5):
    driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]').click()

buttons_del = driver.find_elements(By.CSS_SELECTOR, '.added-manually')
print(len(buttons_del))

# Клик по кнопке без ID
driver.get('http://uitestingplayground.com/dynamicid')
driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

# Клик по кнопке с CSS-классом
driver.get('http://uitestingplayground.com/classattr')
driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

# Модальное окно
try:
    driver.get('http://the-internet.herokuapp.com/entry_ad')
    driver.find_element(By.CSS_SELECTOR, 'modal-footer').click()
except:
    'Какая-то ошибка'    

# Поле ввода
driver.get('http://the-internet.herokuapp.com/inputs')
driver.find_element(By.CSS_SELECTOR, 'input').send_keys('1000')
driver.find_element(By.CSS_SELECTOR, 'input').clear()
driver.find_element(By.CSS_SELECTOR, 'input').send_keys('999')

# Форма авторизации
driver.get('http://the-internet.herokuapp.com/login')
driver.find_element(By.CSS_SELECTOR, '#username').send_keys('tomsmith')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('SuperSecretPassword!')
driver.find_element(By.CSS_SELECTOR, '.radius').click()
 