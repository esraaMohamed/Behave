from BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://www.demo.guru99.com/V4/')

    locator_dictionary = {
        "username": (By.NAME, 'uid'),
        "password": (By.NAME, 'password'),
        "sign_in": (By.NAME, 'btnLogin'),
        "reset": (By.NAME, 'btnReset')
    }

    def input_username(self, username="mngr66332"):
        self.find_element(*self.locator_dictionary['username']).send_keys(username)

    def input_password(self, passwd="vavYren"):
        self.find_element(*self.locator_dictionary['password']).send_keys(passwd)

    def click_sign_in(self):
        self.find_element(*self.locator_dictionary['sign_in']).click()

    def login(self, username="", passwd=""):
        self.find_element(*self.locator_dictionary['username']).send_keys(username)
        self.find_element(*self.locator_dictionary['password']).send_keys(passwd)
        self.find_element(*self.locator_dictionary['sign_in']).click()
