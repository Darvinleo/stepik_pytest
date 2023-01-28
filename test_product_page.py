from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

promo_urls = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
              pytest.param(
                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                  marks=pytest.mark.xfail),
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.need_review
@pytest.mark.parametrize('link', promo_urls)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_bet_add_to_basket_btn()
    main_product_name = product_page.get_product_name()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message()
    assert main_product_name == product_page.get_product_name_from_success_message(), \
        "Product Name in Success Alert not the same as name in Product description"
    assert product_page.get_product_price() == product_page.get_total_basket_price(), \
        "Total basket price is not the same with added Product price"


test_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.need_review
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link=test_url):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser, link=test_url):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link=test_url):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappear_success_message()


url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


def test_guest_should_see_login_link_on_product_page(browser, link=url):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, link=url):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link=url):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_about_empty_basket()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link="http://selenium1py.pythonanywhere.com/accounts/login/"):
        from random_word import RandomWords
        login_page = LoginPage(browser, link)
        login_page.open()
        email = RandomWords().get_random_word() + "_2613@fakemail.org"
        password = RandomWords().get_random_word() + "abra_cadabRA!123"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link=test_url):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket_with_promo(self, browser):
        promo_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
        product_page = ProductPage(browser, promo_link)
        product_page.open()
        product_page.should_bet_add_to_basket_btn()
        main_product_name = product_page.get_product_name()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_success_message()
        assert main_product_name == product_page.get_product_name_from_success_message(), \
            "Product Name in Success Alert not the same as name in Product description"
        assert product_page.get_product_price() == product_page.get_total_basket_price(), \
            "Total basket price is not the same with added Product price"
