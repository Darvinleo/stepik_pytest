from .base_page import BasePage
from .locators import ProductPageLocators
from helpers.help_functions import price_extractor
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
        return price_extractor(raw_price)

    def get_total_basket_price(self):
        price_raw = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_PRICE).text
        return price_extractor(price_raw)

    def should_be_success_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ALERT), "No Success alert !"

    def get_success_alert_text(self):
        text = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT).text
        return text

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
            print("No second alert presented")
