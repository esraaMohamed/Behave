import sys

from behave import given, when, then
from selenium import webdriver

from BDD1.features.lib.pages import LoginPage, HomePage


@given("I open the website")
def open_the_website(context):
    """
    step to create a new user
    :param context:
    :return:
    """
    print("I am opening the website")
    print(sys.path)
    context.browser = webdriver.Firefox()
    page = LoginPage.LoginPage(context=context)
    page.visit("http://www.demo.guru99.com/V4/")
    print("Login page should be open now")


@when("I enter the user name")
def enter_username(context):
    """
    Step to type email address in the email field "username"
    :param context:
    :return:
    """
    print("Typing the email in the username field")
    page = LoginPage.LoginPage(context=context)
    page.input_username(username="mngr66332")
    print("Just finished typing the email in the username field")


@when("I enter the password")
def enter_password(context):
    """
    Step to type password in the password field
    :param context:
    :return:
    """
    print("Typing the password in the password field")
    page = LoginPage.LoginPage(context=context)
    page.input_password(passwd="vavYren")
    print("Just finished typing the password in the password field")


@when("Click on the login button")
def click_login_button(context):
    """
    Step to click on the login button
    :param context:
    :return:
    """
    print("Clicking on the login button")
    page = LoginPage.LoginPage(context=context)
    page.click_sign_in()
    print("Just finished clicking the login button")


@then("I should see a welcome message")
def assert_welcome_message_appears(context):
    """
    Step to assert that the welcome message appears after successful login
    :param context:
    :return:
    """
    page = HomePO.HomePage(context=context)
    assert page.is_welcome_message_displayed(), "the welcome message is not displayed"
    assert page.is_manager_id_valid(manager_id="mngr66332")
