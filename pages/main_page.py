from pages.base_page import BasePage
from locators.locators_main_page import Main_page_locators


class MainPage(BasePage):

    def check_popular_tab(self):
        popular = self.browser.find_element_by_xpath\
            (Main_page_locators.popular_tab)
        assert popular.is_displayed() is True, 'No popular tab'

    def check_bestsellers_tab(self):
        bestsellers = self.browser.find_element_by_xpath\
            (Main_page_locators.best_sellers_tab)
        assert bestsellers.is_displayed() is True, 'No bestsellers tab'

    def check_description(self):
        description = self.browser.find_element_by_xpath\
            (Main_page_locators.description)
        assert description.is_displayed() is True, 'No description'
