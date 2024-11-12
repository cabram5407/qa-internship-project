from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class ProfileChange(Page):
    EDIT_PROF = (By.XPATH,"//a[@class='page-setting-block w-inline-block' and @href='/profile-edit']")


    def profile_edit(self):
        sleep(3)
        self.wait_and_click(*self.EDIT_PROF)
        sleep(3)
