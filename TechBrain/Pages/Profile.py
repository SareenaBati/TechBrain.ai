import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Profile:
    def __init__(self,driver):
        self.driver=driver
        # self.edit_profile =(By.XPATH,'//a[@href="/profile/edit"]')
        # self.first_name = (By.XPATH, '//input[@name="user[first_name]"]')
        # self.last_name = (By.XPATH, '//input[@name="user[last_name]"]')
        # self.email = (By.XPATH, '//input[@name="user[email]"]')
        # self.phone = (By.XPATH, '//input[@name="user[phone]"]')
        # self.address = (By.XPATH, '//input[@name="user[street_address]"]')
        # self.postal_code = (By.XPATH, '//input[@name="user[postalcode]"]')
        # self.city = (By.XPATH, '//input[@name="user[city]"]')
        # self.country = (By.XPATH, '//select[@name="user[country]"]')
        # self.update_profile_button = (By.XPATH, '//input[@name="commit"]')

    def open_profile_page(self,url):
        self.driver.get(url)

    def click_profile(self):
        profile_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='flex text-blue-600 text-lg ml-5']//span[contains(text(),'Profile')]"))
        )
        profile_element.click()

    def click_edit_profile(self):
        edit_profile_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'profile/edit')]"))
        )
        edit_profile_element.click()


    def enter_first_name(self,first_name):
        first_name_element=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="user[first_name]"]')))
        first_name_element.clear()
        first_name_element.send_keys(first_name)


    def enter_last_name(self,last_name):
        last_name_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="user[last_name]"]')))
        last_name_element.clear()
        last_name_element.send_keys(last_name)


    def enter_email(self,email):
        email_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="user[email]"]')))
        email_element.clear()
        email_element.send_keys(email)


    def click_update_profile_button (self):
        update_profile_button_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="commit"]')))
        update_profile_button_element.click()

    def scrolldown(self):
        try:
            page_height = self.driver.execute_script("return document.body.scrollHeight")
            scroll_speed = 1
            scroll_iteration = int(page_height / scroll_speed)
            for _ in range(scroll_iteration):
                self.driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
            time.sleep(1)
        except Exception as e:
            print(f"Error during Scrolling: {e}")



