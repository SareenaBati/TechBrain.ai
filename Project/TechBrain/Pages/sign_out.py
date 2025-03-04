from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignOut:
    def __init__(self, driver):
        self.driver = driver

    def open_sign_out_page(self, url):
        self.driver.get(url)

    def click_sign_out(self):
        sign_out = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='flex text-blue-600 text-lg ml-5']//span[contains(text(),'Sign out')]"))
        )
        sign_out = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//a[@class='flex text-blue-600 text-lg ml-5']//span[contains(text(),'Sign out')]"))
        )
        sign_out.click()

    def handle_alert(self):
        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_message = alert.text
            print(f"Alert Message: {alert_message}")
            alert.accept()
        except Exception as e:
            print(f"No alert found: {e}")
