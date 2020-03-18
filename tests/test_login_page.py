from pages.login_page import LoginPage


def test_login_page(browser):
    url = 'http://automationpractice.com/index.php?controller=' \
          'authentication&back=my-account'
    lp = LoginPage(browser, url)
    lp.url_check_login()
    lp.check_create_acc_test()
    lp.check_already_registered_test()
    lp.login_fail_test()
    lp.login_test()
