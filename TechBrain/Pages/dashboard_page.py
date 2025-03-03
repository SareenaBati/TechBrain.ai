import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Dashboard:
    def __init__(self,driver):
        self.driver=driver

    def open_dashboard_page(self,url):
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

    #coure description block1

    def course_description(self):
        try:
            # Wait until the element is visible
            list_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//a[@class="flex mb-3"]'))
            )

            # Ensure the element is clickable before clicking
            list_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@class="flex mb-3"]'))
            )

            list_element.click()
            time.sleep(2)

            continue_lesson= WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  '//a[@href="/introduction-to-ruby-and-object-oriented-programming/lessons/goals-of-the-intro-course"]'))
            )
            continue_lesson = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//a[@href="/introduction-to-ruby-and-object-oriented-programming/lessons/goals-of-the-intro-course"]'))
            )
            continue_lesson.click()
            time.sleep(2)
            self.scrolldown()



        except Exception as e:
            print(f"Error while clicking : {e}")




