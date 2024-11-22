from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class ProfileChange(Page):
    # EDIT_PROF = (By.XPATH,"//a[@class='page-button-menu w-inline-block' and @href='/profile-edit']")
    EDIT_PROF = (By.CSS_SELECTOR, 'a[href="/profile-edit"]')
    # EDIT_PROF = (By.XPATH, "//div[@wized='clientModeButton']")


    def profile_edit(self):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, 100);")
        self.wait_and_click(*self.EDIT_PROF)
        sleep(3)
