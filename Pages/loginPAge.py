from selenium.webdriver.common.by import By
from .basePage import BasePage

class Loginpage(BasePage):
    SIGN_IN_BUTTON = (By.ID, "nav-link-accountList-nav-line-1")
    EMAIL_FIELD = (By.XPATH, "//input[@id='ap_email']")
    CONTINUE_BUTTON = (By.ID, "continue")
    PASSWORD_FIELD = (By.ID, "ap_password")
    SUBMIT_BUTTON = (By.ID, "signInSubmit")


    def click_signin(self):

        self.click(self.SIGN_IN_BUTTON)

    def enter_email(self, email):
        self.send_keys(self.EMAIL_FIELD, email)
        self.click(self.CONTINUE_BUTTON)

    def enter_pass_and_submit(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.SUBMIT_BUTTON)


