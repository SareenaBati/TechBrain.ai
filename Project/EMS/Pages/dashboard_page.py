from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait




class Dashboard:
    def __init__(self, driver):
        self.driver = driver

    def open_dashboard_page(self, url):
        self.driver.get(url)

