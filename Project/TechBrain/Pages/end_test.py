import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EndTest:
    def __init__(self,driver):
        self.driver=driver



    def open_end_test_page(self,url):
        self.driver.get(url)

    def click_verify(self):
        verify_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="email_subject"]'))
        )
        verify_email.click()
