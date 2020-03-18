from pages.base_page import BasePage
from locators.locators_login_page import Login_page_locators


class LoginPage(BasePage):

    def url_check_login(self):
        self.go_to_site()
        url1 = self.url
        assert url1 == "http://automationpractice.com/index.php?" \
                       "controller=authentication&back=my-account"

    def check_create_acc_test(self):
        self.go_to_site()
        create_acc = self.browser.find_element_by_xpath \
            (Login_page_locators.create_account)
        assert create_acc.is_displayed(), 'No create ' \
                                          'acc message'

    def check_already_registered_test(self):
        self.go_to_site()
        already_reg = self.browser.find_element_by_xpath \
            (Login_page_locators.already_registered)
        assert already_reg.is_displayed(), 'No create acc message'

    def login_test(self):
        self.go_to_site()
        email = self.browser.find_element_by_xpath \
            (Login_page_locators.login)
        email.send_keys('sergey@test.com')
        password = self.browser.find_element_by_xpath \
            (Login_page_locators.password)
        password.send_keys('test123')
        sign_in = self.browser.find_element_by_xpath \
            (Login_page_locators.sign_in_button)
        sign_in.click()
        message = self.browser.find_element_by_xpath \
            (Login_page_locators.logged_in_message)
        assert message.is_displayed(), \
            'No message for logged in user'

    def login_fail_test(self):
        self.go_to_site()
        email = self.browser.find_element_by_xpath \
            (Login_page_locators.login)
        email.send_keys('sergey@fail.com')
        password = self.browser.find_element_by_xpath \
            (Login_page_locators.password)
        password.send_keys('test123')
        sign_in = self.browser.find_element_by_xpath \
            (Login_page_locators.sign_in_button)
        sign_in.click()
        message = self.browser.find_element_by_xpath \
            (Login_page_locators.sign_in_failed)
        assert message.is_displayed(), 'No error message'
