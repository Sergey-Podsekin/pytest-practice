class Login_page_locators:
    sign_in = "//*[@class='login']"
    create_account = "//*[@class='page-subheading'][contains(text(), 'Create')]"
    already_registered = "//*[@class='page-subheading'][contains(text(), 'Already')]"
    login = "//*[@id='email']"
    password = "//*[@id='passwd']"
    logged_in_message = "//*[@class='info-account']"
    sign_in_button = "//*[@id='SubmitLogin']"
    sign_in_failed = "//*[@class='alert alert-danger']/ol/li"
