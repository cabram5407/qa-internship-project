from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):
    EMAIL = (By.CSS_SELECTOR, "input#email-2.input.w-input")
    PSWD = (By.XPATH, "//input[@wized='passwordInput']")
    LOGIN_BTN = (By.XPATH, "//a[@wized='loginButton']")

    def input_login_information(self):
        sleep(3)
        self.input_text("cabram1967@comcast.net", *self.EMAIL)
        self.input_text("Blkgrl@Rck5407!", *self.PSWD)
        sleep(3)
        self.wait_to_be_clickable_click(*self.LOGIN_BTN)
        sleep(3)