from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from time import sleep


class LoginPage(Page):
    EMAIL = (By.CSS_SELECTOR, "input#email-2.input.w-input")
    PSWD = (By.XPATH, "//input[@wized='passwordInput']")
    LOGIN_BTN = (By.XPATH, "//a[@wized='loginButton']")

    def open_page(self):
         sleep(2)
         self.open('https://soft.reelly.io')
         sleep(3)


    def input_login_information(self):
        self.input_text("cabram1967@comcast.net", *self.EMAIL)
        self.input_text("Blkgrl@Rck5407!", *self.PSWD)
        sleep(3)
        self.wait_and_click(*self.LOGIN_BTN)
        sleep(3)