from pages.base_page import BasePage
from locators.locators_cart_page import Cart_page_locators


class CartPage(BasePage):

    def empty_cart(self):
        self.go_to_site()
        cart1 = self.browser.find_element_by_xpath \
            (Cart_page_locators.empty_cart)
        assert cart1.is_displayed() is True, \
            'No empty cart message'

    def cart_summary(self):
        self.go_to_site()
        cart2 = self.browser.find_element_by_xpath \
            (Cart_page_locators.cart_summary_message)
        assert cart2.is_displayed() is True, \
            'No cart summary message'

    def your_cart(self):
        self.go_to_site()
        cart3 = self.browser.find_element_by_xpath \
            (Cart_page_locators.your_shopping_cart)
        assert cart3.is_displayed() is True, \
            'No your cart message'

    def add_item(self):
        add_item_to_cart = self.browser.find_element_by_xpath \
            (Cart_page_locators.add_to_cart)
        add_item_to_cart.click()
        self.go_to_site()
        cart4 = self.browser.find_element_by_xpath \
            (Cart_page_locators.product_in_cart)
        assert cart4.is_displayed() is True, 'No your cart message'
