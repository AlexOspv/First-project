from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time

class ProductPage(BasePage):
    def add_book_to_basket(self):
        ProductPage.should_be_add_to_basket_button(self)
        ProductPage.click_add_to_basket_button(self)
        #ProductPage.solve_quiz_and_get_code(self)
        #time.sleep(5)
        ProductPage.should_be_name_book_in_message(self)
        ProductPage.should_be_value_price_in_message(self)

    def value_price(self):
        return self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).text

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "'Add to basket button is missing"

    def click_add_to_basket_button(self):
        return self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def should_be_name_book_in_message(self):
        name_book = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        print(name_book)
        name_book_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_MSG).text
        print(name_book_message)
        assert name_book == name_book_message, "Invalid book's name"

    def should_be_value_price_in_message(self):
        value_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        print(value_price)
        value_price_message = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_MSG).text
        print(value_price_message)
        assert value_price == value_price_message, "Invalid basket's price"
   
    def should_not_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    #def should_be_success_message(self):
        #assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            #"Success message is presented, but should not be"