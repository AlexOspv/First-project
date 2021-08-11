from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    REGISTER_MAIL = (By.NAME, "registration-email")
    REGISTER_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTER_PASSWORD2 = (By.NAME, "registration-password2")

class ProductPageLocators():
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME_MSG = (By.CSS_SELECTOR, ".alertinner > strong")
    BOOK_PRICE_MSG = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert-success')
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR,".basket-mini > span > a")

class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR,"#content_inner > .basket-title")
    BASKET_CONTENT_MSG =(By.CSS_SELECTOR,"#content_inner > p")
    