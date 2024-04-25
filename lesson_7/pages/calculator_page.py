from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator_page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        
    def prep(self):
        '''
        Подготовка калькулятора для вычислений
        очистка и задание задержки
        '''
        self.driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('4')
        
        
    def btns_clickng(self,click_list):
        '''
        Нажатие на лист кнопок по очереди
        '''
        for i in click_list:
            self.driver.find_element(By.XPATH, i).click()
            
    def get_result(self):
        '''
        Нахождение результата вычислений
        '''
        WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[style = "display: none;"]'))
        )
        
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text