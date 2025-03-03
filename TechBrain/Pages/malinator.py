from selenium import webdriver
from selenium.webdriver.common.by import By


import time
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.mailinator.com/")
    driver.maximize_window()
    return driver

