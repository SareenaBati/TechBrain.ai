import time
from selenium.webdriver.common.by import By

class ForgetPassword:
    def __init__(self,driver):
        self.driver=driver
        self.sign_in = (By.XPATH, '//a[@href="/users/sign_in"]')
        self.forget_your_password=(By.XPATH,'//a[@class="text-gray-500 text-sm"]')
        self.email=(By.XPATH,'//input[@id="user_email"]')
        self.submit=(By.XPATH,'//input[@type="submit"]')

    def open_forget_password_page(self, url):
        self.driver.get(url)

    def click_sign_in(self):
        self.driver.find_element(*self.sign_in).click()

    def click_forget_your_password(self):
        self.driver.find_element(*self.forget_your_password).click()

    def enter_email(self,email):
        self.driver.find_element(*self.email).send_keys(email)
    def click_submit(self):
        self.driver.find_element(*self.submit).click()
