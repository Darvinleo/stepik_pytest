from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
    MAIN_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MAIN_PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_ALERT = (By.XPATH, "//*[@id='messages']/div[1]")
    PRODUCT_NAME_FROM_SUCCESS_ALERT = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
