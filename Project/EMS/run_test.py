import pytest
from selenium import webdriver
from Automation.Project.EMS.Pages.login_page import LoginPage
from Automation.Project.EMS.Pages.forget_password_page import ForgetPassword
import time




@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page("https://namespace-team.github.io/ems-web/login")
    login_page.enter_email("testuser@namespace.jp")
    login_page.enter_password("p@ssw0rD44")
    login_page.click_sign_in()

def test_forget_password(driver):
    forget_password_page=ForgetPassword(driver)
    forget_password_page.open_forget_password_page("https://namespace-team.github.io/ems-web/login")
    forget_password_page.click_forget_password()

@pytest.fixture(scope="function")
def signin(driver):

def test_dashboard_page(driver):


