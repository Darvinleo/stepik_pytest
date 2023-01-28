from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def should_bet_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "No Add to basket button"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT_NAME).text

    def get_product_price(self):
        raw_price = self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT_PRICE).text
        return self.price_extractor(raw_price)

    def get_total_basket_price(self):
        raw_price = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_PRICE).text
        return self.price_extractor(raw_price)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_ALERT), "Success message should disappear, but it's not"

    def get_success_message_full_text(self):
        text = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT).text
        return text

    def get_product_name_from_success_message(self):
        text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_SUCCESS_ALERT).text
        return text

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), "Success message should disappear, but it not"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            pass
