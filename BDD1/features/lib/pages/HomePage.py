from selenium.webdriver.common.by import By

from BasePage import BasePage


class HomePage(BasePage):
    locator_dictionary = {
        "welcome_message": (By.TAG_NAME, 'marquee'),  # Welcome To Manager's Page of Guru99 Bank
        "manager_id": (By.CSS_SELECTOR, 'td[style="color: green"]')
    }

    # title :  Guru99 Bank Manager HomePage

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://www.demo.guru99.com/V4/')

    def is_welcome_message_displayed(self):
        return self.find_element(*self.locator_dictionary['welcome_message']).is_displayed()

    def is_manager_id_valid(self, manager_id):
        if manager_id in self.find_element(*self.locator_dictionary["manager_id"]).text:
            return True
        else:
            raise AssertionError('manager id is not displayed')


