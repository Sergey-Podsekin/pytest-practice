class Cart_page_locators:
    empty_cart = "//*[@class='alert alert-warning']"
    cart_summary_message = "//*[@id='cart_title']"
    your_shopping_cart = "//*[@class = 'breadcrumb clearfix']"
    add_to_cart = "//*[@id='homefeatured']/li[1]//*[contains" \
                  "(text(),'Add to cart')]"
    product_in_cart = '//*[@id="summary_products_quantity"]'
    first_item = "//*[@id='homefeatured']/li[1]/div/div[2]"
    proceed_to_checkout = "//*[@id='layer_cart']//a"
