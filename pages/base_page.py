class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def find_element(self, locator):
        self.browser.find_element_by_xpath(self, locator)

    def go_to_site(self):
        self.browser.get(self.url)
        return True

    def url(self):
        return self.browser.current_url
