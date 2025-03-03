import time
import pytest
from selenium import webdriver

from Project.TechBrain.Pages.sign_in_page import SignIn
from Project.TechBrain.Pages.dashboard_page import Dashboard
from Project.TechBrain.Pages.sign_up import SignUp
from Project.TechBrain.Pages.sign_out import SignOut
from Project.TechBrain.Pages.forget_password import ForgetPassword
from Project.TechBrain.Pages.Profile import Profile
from Project.TechBrain.Pages.Quiz import Quiz




@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    # driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()




def test_sign_up_page(driver):
    sign_up_page=SignUp(driver)
    sign_up_page.open_sign_up_page("https://techbrain.ai/")
    driver.maximize_window()
    sign_up_page.click_sign_in()
    sign_up_page.click_sign_up()
    sign_up_page.enter_email("ketax62300@endtest-mail.io")
    sign_up_page.enter_password("Sarinagmail@9#")
    sign_up_page.enter_password_confirmation("Sarinagmail@9#")
    sign_up_page.click_sign_up_button()
    time.sleep(5)
    sign_up_page.open_sign_up_page("https://app.endtest.io/mailbox?email=ketax62300@endtest-mail.io")
    sign_up_page.click_verify()
    sign_up_page.click_mail_link()
    sign_up_page.enter_email1("sareena.bati@gmail.com")
    sign_up_page.enter_password1("Sarinagmail@9#")
    sign_up_page.login_button()
    time.sleep(5)




def test_sign_in_page(driver):
    sign_in_page=SignIn(driver)
    sign_in_page.open_sign_in_page("https://techbrain.ai/")
    driver.maximize_window()
    sign_in_page.click_sign_in()
    sign_in_page.enter_email("sareena.bati@gmail.com")
    sign_in_page.enter_password("Sarinagmail@9#")
    sign_in_page.click_login()
    time.sleep(2)




@pytest.fixture(scope="module")
def signin(driver):

    sign_in_page = SignIn(driver)
    driver.maximize_window()
    sign_in_page.open_sign_in_page("https://techbrain.ai/")
    sign_in_page.click_sign_in()
    sign_in_page.enter_email("sareena.bati@gmail.com")
    sign_in_page.enter_password("Sarinagmail@9#")
    sign_in_page.click_login()
    return driver


def test_forget_password(signin,driver):

    forget_password = ForgetPassword(signin)

    # forget_password.open_forget_password_page("https://techbrain.ai/")
    forget_password.click_sign_in()
    forget_password.click_forget_your_password()
    forget_password.enter_email("sareena.bati@gmail.com")
    forget_password.click_submit()


def test_profile_page(signin,driver):

    profile_page = Profile(signin)
    profile_page.click_profile()
    profile_page.click_edit_profile()
    profile_page.enter_first_name("User")
    profile_page.enter_last_name("user")
    profile_page.enter_email("user@example.com")
    profile_page.scrolldown()
    profile_page.click_update_profile_button()


def test_dashboard_page(signin,driver):
    dashboard_page=Dashboard(signin)
    dashboard_page.open_dashboard_page("https://techbrain.ai/")
    driver.maximize_window()
    dashboard_page.scrolldown()
    dashboard_page.course_description()

def test_quiz_page(signin,driver):
    quiz_page=Quiz(signin)
    quiz_page.open_quiz_page("https://techbrain.ai/introduction-to-ruby-and-object-oriented-programming/lessons/hashes")
    driver.maximize_window()
    # quiz_page.scrolldown()
    quiz_page.Quiz()

# def test_end_test_page(driver):
#     end_test_page=EndTest(driver)
#     end_test_page.open_end_test_page("https://app.endtest.io/mailbox?email=ketax62300@endtest-mail.io")
#     end_test_page.click_verify()
#     driver.maximize_window()















