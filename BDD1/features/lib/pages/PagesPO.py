
"""class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    def navigate(self):
        self.driver.get("http://www.demo.guru99.com/V4/")

    def set_username(self, username):
        username_field = self.driver.find_element('name', 'uid')
        username_field.send_keys(username)

    def set_password(self, password):
        password_field = self.driver.find_element('name', 'password')
        password_field.send_keys(password)

    def click_submit(self):
        submit_button = self.driver.find_element('name', 'btnLogin')
        submit_button.click()

    def click_reset(self):
        submit_button = self.driver.find_element('name', 'btnReset')
        submit_button.click()

"""
"""class HomePage(BasePage):
    def is_header_present(self):
        header = self.driver.find_element_by_tag_name('h2')
        if header.text == "Guru99 Bank":
            return True
        else:
            raise AssertionError("Not in the home page")

    def manager_id_correct(self, manager_id):
        manager_id_field = self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[3]/td")
        if manager_id_field.text == manager_id:
            return True
        else:
            raise AssertionError("Not in the home page")
            """