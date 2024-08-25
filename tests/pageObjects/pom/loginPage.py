# Login Page Class
import time

# Page Locators
# Page Actions

# WebDriver Init
# Custom Functions
# No assertions(in Page Object Class)

# get email and send keys - email
# get password and send keys - password
# case 1 - click the submit button and navigate to dashboard Page
# case 2 - invalid -> error message


from selenium.webdriver.common.by import By
from tests.utils.common_utils import webdriver_wait


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

        # Page Locator
    test_username_id = (By.ID,"login-username")
    text_password_id = (By.NAME,"password")
    #button_forgot_password_xpath= (By.XPATH,"//button[text()='Forgot Password?']")
    submit_button_xpath = (By.XPATH, "//button[@id='js-login-btn']")
    error_message_cssselector = (By.CSS_SELECTOR,"#js-notification-box-msg")

        # Page Actions

    def get_username(self):
        return self.driver.find_element(*LoginPage.test_username_id)

    def get_password(self):
        return self.driver.find_element(*LoginPage.text_password_id)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button_xpath)

    def get_error_message(self):
        webdriver_wait(driver=self.driver,elemtn_tuple=self.get_error_message())
        return self.driver.find_element(*LoginPage.error_message_cssselector)

    def login_to_vwo(self,username,password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_submit_button().click()


    def get_error_message_text(self):
        return self.get_error_message().text


