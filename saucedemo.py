import time
from data.reading_excel import demo_locators
from library.selenium_wrapper import SeleniumWrapper

locators = demo_locators()

class SauceDemoLogin:

    def __init__(self, driver):
        self.driver = driver
        self.sel_wrap_obj = SeleniumWrapper(self.driver)

    def username(self):
        self.sel_wrap_obj.enter_data(locators['text_username'], 'standard_user')

    def password(self):
        self.sel_wrap_obj.enter_data(locators['text_pwd'], 'secret_sauce')

    def login_button(self):
        self.sel_wrap_obj.click_element(locators['btn_login'])
        time.sleep(3)

    def verify_login(self):
        assert self.driver.find_element(*locators['verify_element'])


class SauceDemoLogout:

    def __init__(self, driver):
        self.driver = driver
        self.sel_wrap_obj = SeleniumWrapper(self.driver)

    def menu_btn(self):
        self.sel_wrap_obj.click_element(locators['btn_menu'])

    def logout(self):
        self.sel_wrap_obj.click_element(locators['btn_logout'])

































