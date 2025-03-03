from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUp:
    def __init__(self,driver):
        self.driver=driver
        # self.sign_in=(By.XPATH,'//a[@href="/users/sign_in"]')
        # self.sign_up=(By.XPATH,'//a[@href="/users/sign_up"]')
        # self.email=(By.XPATH,'//input[@id="user_email"]')
        # self.password=(By.XPATH,'//input[@id="user_password"]')
        # self.password_confirmation=(By.XPATH,'//input[@id="user_password_confirmation"]')
        # self.sign_up_button=(By.XPATH,'//input[@type="submit"]')

    def open_sign_up_page(self,url):
        self.driver.get(url)

    def click_sign_in(self):
        sign_in=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//a[@href="/users/sign_in"]')))
        sign_in.click()


    def click_sign_up(self):
        sign_up=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//a[@href="/users/sign_up"]')))
        sign_up.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Sign up')]")))

    def enter_email(self,email):
        email_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@id="user_email"]')))
        email_element.send_keys(email)

    def enter_password(self, password):
        password_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@id="user_password"]')))
        password_element.send_keys(password)

    def enter_password_confirmation(self, password_confirmation):
        password_confirmation_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'//input[@id="user_password_confirmation"]')))
        password_confirmation_element.send_keys(password_confirmation)

    def click_sign_up_button(self):
        sign_up_element=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="submit"]')))
        sign_up_element.click()

    def click_verify(self):
        verify_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="email_subject"]'))
        )
        verify_email.click()

    def click_mail_link(self):
        mail_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//a)[1]'))
        )
        mail_link.click()

    def click_login(self):
        login=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//a[@href="/users/sign_in"]')))
        login.click()

    def enter_email1(self, email1):
        email_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="user_email"]')))
        email_element.send_keys(email1)

    def enter_password1(self, password1):
        password_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="user_password"]')))
        password_element.send_keys(password1)

    def login_button(self):
        login_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="submit"]')))
        login_element.click()

