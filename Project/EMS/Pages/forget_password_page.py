from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait




class ForgetPassword:
    def __init__(self, driver):
        self.driver = driver

    def open_forget_password_page(self, url):
        self.driver.get(url)

    def click_forget_password(self):
        forget_password=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//a[@class="text-red-700 font-bold underline"]'))
        )
        forget_password.click()