from pages.cart_page import CartPage


def test_login_page(browser):
    url = 'http://automationpractice.com/index.php?controller=order'
    cp = CartPage(browser, url)
    cp.cart_summary()
    cp.empty_cart()
    cp.your_cart()
    cp.add_item()
