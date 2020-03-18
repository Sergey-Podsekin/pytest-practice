from pages.main_page import MainPage


def test_main_page(browser):
    url = 'http://automationpractice.com/index.php'
    mp = MainPage(browser, url)
    mp.check_popular_tab()
    mp.check_bestsellers_tab()
    mp.check_description()
