import pytest
from selenium import webdriver
from Automation.Project.TechBrain.Pages.sign_in_page import SignIn
from Automation.Project.TechBrain.Pages.dashboard_page import Dashboard
from Automation.Project.TechBrain.Pages.sign_up import SignUp
from Automation.Project.TechBrain.Pages.sign_out import SignOut
from Automation.Project.TechBrain.Pages.forget_password import ForgetPassword
from Automation.Project.TechBrain.Pages.Profile import Profile
from Automation.Project.TechBrain.Pages.Quiz import Quiz
import time

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def signin(driver):
    sign_in_page = SignIn(driver)
    sign_in_page.open_sign_in_page("https://techbrain.ai/")
    sign_in_page.click_sign_in()
    sign_in_page.enter_email("ketax62300@endtest-mail.io")
    sign_in_page.enter_password("Sarinagmail1@")
    sign_in_page.click_login()
    return driver


def test_sign_up_page(driver):
    sign_up_page = SignUp(driver)
    sign_up_page.open_sign_up_page("https://techbrain.ai/")
    sign_up_page.click_sign_in()
    sign_up_page.click_sign_up()
    sign_up_page.enter_email("ketax62300@endtest-mail.io")
    sign_up_page.enter_password("Sarinagmail@9#")
    sign_up_page.enter_password_confirmation("Sarinagmail@9#")
    sign_up_page.click_sign_up_button()
    sign_up_page.open_sign_up_page("https://app.endtest.io/mailbox?email=ketax62300@endtest-mail.io")
    sign_up_page.click_verify()
    sign_up_page.click_mail_link()
    sign_up_page.enter_email1("ketax62300@endtest-mail.io")
    sign_up_page.enter_password1("Sarinagmail@9#")
    sign_up_page.login_button()



def test_sign_in_page(driver):
    sign_in_page = SignIn(driver)
    sign_in_page.open_sign_in_page("https://techbrain.ai/")
    sign_in_page.click_sign_in()
    sign_in_page.enter_email("ketax62300@endtest-mail.io")
    sign_in_page.enter_password("Sarinagmail1@")
    sign_in_page.click_login()


def test_dashboard_page(signin, driver):
    dashboard_page = Dashboard(driver)
    dashboard_page.open_dashboard_page("https://techbrain.ai/")
    dashboard_page.scrolldown()
    dashboard_page.course_description()


def test_quiz_page(signin, driver):
    quiz_page = Quiz(driver)
    quiz_page.open_quiz_page("https://techbrain.ai/introduction-to-ruby-and-object-oriented-programming/lessons/hashes")
    quiz_page.Quiz()


def test_forget_password(driver):
    forget_password = ForgetPassword(driver)
    forget_password.open_forget_password_page("https://techbrain.ai/")
    forget_password.click_sign_in()
    forget_password.click_forget_your_password()
    forget_password.enter_emails("ketax62300@endtest-mail.io")
    forget_password.click_submit()
    forget_password.open_forget_password_page("https://app.endtest.io/mailbox?email=ketax62300@endtest-mail.io")
    forget_password.click_verify()
    forget_password.click_mail_link()
    forget_password.enter_new_password("Sarinagmail1@")
    forget_password.enter_confirm_password("Sarinagmail1@")
    forget_password.click_update_password()


def test_profile_page(signin, driver):
    profile_page = Profile(driver)
    profile_page.click_profile()
    profile_page.click_edit_profile()
    profile_page.enter_first_name("User")
    profile_page.enter_last_name("User")
    profile_page.enter_email("user@example.com")
    profile_page.scrolldown()
    profile_page.click_update_profile_button()


def test_sign_out_page(signin, driver):
    sign_out_page = SignOut(driver)
    sign_out_page.click_sign_out()
    sign_out_page.handle_alert()
