from pages.base_page import BasePage
from locators.locators_cart_page import Cart_page_locators
from selenium.webdriver.common.action_chains import ActionChains


class CartPage(BasePage):

    def empty_cart(self):
        self.go_to_site()
        cart1 = self.browser.find_element_by_xpath \
            (Cart_page_locators.empty_cart)
        assert cart1.is_displayed(), \
            'No empty cart message'

    def cart_summary(self):
        self.go_to_site()
        cart2 = self.browser.find_element_by_xpath \
            (Cart_page_locators.cart_summary_message)
        assert cart2.is_displayed(), \
            'No cart summary message'

    def your_cart(self):
        self.go_to_site()
        cart3 = self.browser.find_element_by_xpath \
            (Cart_page_locators.your_shopping_cart)
        assert cart3.is_displayed(), \
            'No your cart message'

    def add_item(self):
        self.url = 'http://automationpractice.com/index.php'
        self.go_to_site()
        first_item = self.browser.find_element_by_xpath \
            (Cart_page_locators.first_item)
        add_item_to_cart = self.browser.find_element_by_xpath \
            (Cart_page_locators.add_to_cart)
        proceed = self.browser.find_element_by_xpath \
            (Cart_page_locators.proceed_to_checkout)
        hover = ActionChains(self.browser).move_to_element(first_item).click(add_item_to_cart)
        hover.perform()
        proceed.click()
        product_in_cart = self.browser.find_element_by_xpath \
            (Cart_page_locators.product_in_cart)
        assert product_in_cart.is_displayed(), 'No your cart message'
