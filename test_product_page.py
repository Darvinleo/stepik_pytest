from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.should_bet_add_to_basket_btn()
    main_product_name = product_page.get_product_name()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_alert()
    assert main_product_name in product_page.get_success_alert_text(), \
        "Not find added Product Name in Success Alert"
    assert product_page.get_product_price() == product_page.get_total_basket_price(), \
        "Total basket price is not the same with added Product price"