from behave import given, when, then
from random import randint

'''driver = webdriver.Firefox()
url = ""
driver.get(url)'''


@given("I generated a random email address")
def generate_a_random_email_address(context):
    """
    step to create a new user
    :param context:
    :return:
    """
    print("I am creating a new user")
    email_address = str(randint(1, 10))+"@domain.com"
    # user.user_creator()


@when("I enter the email in the username field")
def enter_username(context):
    """
    Step to type email address in the email field "username"
    :param context:
    :return:
    """
    print("Typing the email in the username field")
    # email_field = driver.find_element('id', 'email')
    # email_field.send_keys(email_address)
    print("Just finished typing the email in the username field")


@when("I enter the password in the password field")
def enter_password(context):
    """
    Step to type password in the password field
    :param context:
    :return:
    """
    print("Typing the password in the password field")
    # password_field = driver.find_element('id', 'password')
    # password_field.send_keys("123456")
    print("Just finished typing the password in the password field")


@when("Click on the signup button")
def click_signup_button(context):
    """
    Step to click on the login button
    :param context:
    :return:
    """
    print("Clicking on the signup button")
    # signup_button = driver.find_element('id', 'signup')
    # signup_button.click()
    print("Just finished clicking the signup button")
