import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ForgetPassword:
    def __init__(self,driver):
        self.driver=driver
        # self.sign_in = (By.XPATH, '//a[@href="/users/sign_in"]')
        # self.forget_your_password=(By.XPATH,'//a[@class="text-gray-500 text-sm"]')
        # self.email=(By.XPATH,'//input[@id="user_email"]')
        # self.submit=(By.XPATH,'//input[@type="submit"]')

    def open_forget_password_page(self, url):
        self.driver.get(url)

    def click_sign_in(self):

        sign_in = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/users/sign_in"]'))
            )
        sign_in.click()


    def click_forget_your_password(self):
        forget_your_password = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'//a[@class="text-gray-500 text-sm"]'))
        )
        forget_your_password.click()

    def enter_emails(self,email):
        email_element= WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='user_email']"))
        )
        email_element.send_keys(email)

    def click_submit(self):
        submit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'//input[@type="submit"]'))
        )
        submit.click()

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

    def enter_new_password(self,new_password):
        new_password_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID,"user_password"))
        )
        new_password_element.send_keys(new_password)

    def enter_confirm_password(self, confirm_password):
        confirm_password_element= WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID,"user_password_confirmation"))
        )
        confirm_password_element.send_keys(confirm_password)

    def click_update_password(self):
        update_password_element= WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@type='submit']"))
        )
        update_password_element.click()


