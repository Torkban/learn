from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Filling_page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        
        
    def filling_inputs(self,input_dict:dict):
        '''
        Ввод значений из словаря по очереди
        '''
        for k,i in input_dict.items():
            self.driver.find_element(By.CSS_SELECTOR, k).send_keys(i)
            
            
    def clicking_btn(self, btn:str):
        '''
        Нажатие на кнопку
        '''
        self.driver.find_element(By.CSS_SELECTOR, btn).click()
        
        
    def get_green(self):
        '''
        Получение списка id полей прошедших валидацию
        '''
        list_g = self.driver.find_elements(By.CSS_SELECTOR, '.alert-success')
        result_list = []
        for i in list_g:
            result_list.append(i.get_attribute('id'))
        return result_list
    
    
    def get_red(self):
        '''
        Получение списка id полей не прошедших валидацию
        '''
        list_r = self.driver.find_elements(By.CSS_SELECTOR, '.alert-danger')
        result_list = []
        for i in list_r:
            result_list.append(i.get_attribute('id'))
        return result_list
        