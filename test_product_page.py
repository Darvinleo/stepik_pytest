from .pages.product_page import ProductPage
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


# @pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_bet_add_to_basket_btn()
    main_product_name = product_page.get_product_name()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_alert()
    assert main_product_name == product_page.get_success_alert_text(), \
        "Not find added Product Name in Success Alert"
    assert product_page.get_product_price() == product_page.get_total_basket_price(), \
        "Total basket price is not the same with added Product price"
