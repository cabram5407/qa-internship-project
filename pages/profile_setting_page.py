from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class SettingPage(Page):
    SETTING_BTN = (By.XPATH, "//div[text()='Settings']")


    def navigate_to_setting(self):
        sleep(5)
        self.wait_and_click(*self.SETTING_BTN)
        sleep(3)


