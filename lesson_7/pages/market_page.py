from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Market_page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')
        

    def filling_inputs(self,input_dict:dict):
        '''
        Ввод значений из словаря по очереди
        '''
        for k,i in input_dict.items():
            self.driver.find_element(By.CSS_SELECTOR, k).send_keys(i)


    def clickings_btns(self,click_list:list):
        '''
        Нажатие на лист кнопок по очереди
        '''
        for i in click_list:
            self.driver.find_element(By.CSS_SELECTOR, i).click()
            
    def clicking_btn(self, btn:str):
        '''
        Нажатие на кнопку
        '''
        self.driver.find_element(By.CSS_SELECTOR, btn).click()
        
        
    def get_result(self):
        '''
        Нахождение итоговой стоимости
        '''
        return self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text