import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Quiz:
    def __init__(self,driver):
        self.driver=driver

    def open_quiz_page(self,url):
        self.driver.get(url)

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

    def Quiz(self):

        try:
            go_to_quiz = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/introduction-to-ruby-and-object-oriented-programming/lessons/hashes/quiz']"))
            )


            go_to_quiz = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/introduction-to-ruby-and-object-oriented-programming/lessons/hashes/quiz']"))
            )

            go_to_quiz.click()



            quiz_checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@id="option-24-93"]'))
            )
            quiz_checkbox.click()
            time.sleep(2)


            submit = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]'))
            )

            submit = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
            )
            submit.click()



        except Exception as e:
            print(f"Error while clicking : {e}")
