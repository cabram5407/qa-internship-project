from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class SettingPage(Page):
    # SETTING_BTN = (By.XPATH, "//div[text()='Settings']")
    SETTING_BTN = (By.XPATH, "//a[@class='assistant-button w-inline-block' and @href='/main-menu']")
    OPEN_SETTING_BTN =(By.XPATH,"//a[@class='menu-photo_avatar w-inline-block' and @href='/settings']")

    def navigate_to_setting(self):
        sleep(5)
        self.wait_and_click(*self.SETTING_BTN)
        self.wait_and_click(*self.OPEN_SETTING_BTN)


