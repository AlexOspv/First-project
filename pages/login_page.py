from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Wrong url, try again"
         
    def should_be_login_form(self):
        login_username = self.is_element_present(*LoginPageLocators.LOGIN_USERNAME)
        login_password = self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)
        assert login_username and login_password, "Login form is missing "
        
    def should_be_register_form(self):
        register_mail = self.is_element_present(*LoginPageLocators.REGISTER_MAIL)
        register_password1 = self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD1)
        register_password2 = self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD2)
        assert register_mail and register_password1 and register_password2, "Register form is missing "