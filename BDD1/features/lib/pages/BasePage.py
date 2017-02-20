
class BasePage(object):
    def __init__(self, browser, base_url='http://www.demo.guru99.com/V4/'):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 30

    def visit(self, url):
        self.browser.get(url)


