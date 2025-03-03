from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait




class SignIn:
    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(driver, 10)


    def open_sign_in_page(self, url):
        self.driver.get(url)

    def click_sign_in(self):
        sign_in_element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/users/sign_in"]')))
        sign_in_element.click()


    def enter_email(self, email):
        email_element=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user_email"]')))

        email_element.send_keys(email)

    def enter_password(self, password):
        password_element=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user_password"]')))

        password_element.send_keys(password)

    def click_login(self):
        login_element=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="submit"]')))
        login_element.click()

