
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback
import time


class BasePage(object):
    def __init__(self, browser, base_url='http://www.demo.guru99.com/V4/'):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 30

    def visit(self, url):
        # time.sleep(10)
        self.browser.get(url)

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def hover(self, element):
        ActionChains(self.browser).move_to_element(element).perform()
        # I don't like this but hover is sensitive and needs some sleep time
        time.sleep(5)

    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
                # I could have returned element, however because of lazy loading, I am seeking the element before return
                return self.find_element(*self.locator_dictionary[what])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print "No %s here!" % what

    def wait_for_element(self, by, value):
        element = WebDriverWait(self.browser, 2).until(
            EC.presence_of_element_located((by, value))
        )
        return element
