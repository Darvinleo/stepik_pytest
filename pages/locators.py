from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    SUCCESS_REGISTRATION_ALERT = (By.CSS_SELECTOR, "div.alert-success")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
    MAIN_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MAIN_PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_ALERT = (By.XPATH, "//*[@id='messages']/div[1]")
    PRODUCT_NAME_FROM_SUCCESS_ALERT = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
