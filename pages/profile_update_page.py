from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from time import sleep


class ProfileUpdatePage(Page):
    AGENT_NAME = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='Fullname']")
    PHONE = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='number']")
    CMPY = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='Company name']")
    YR_JOINED = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='When Joined Company 2']")
    CNT_EMAIL = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='Email 2']")
    LANGUAGE = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='Languages']")
    LIC_NUM = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='When joined company']")
    SOC_MEDIA = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='Email']")

    SAVE_BTN = (By.CSS_SELECTOR, "div.save-changes-button[wized='saveButtonProfile']")
    CLOSE_BTN = (By.CSS_SELECTOR, "a.close-button.w-button[href='/settings']")


    def input_fields(self):
        sleep(3)
        self.input_text("test+Charmaine Abram+careerist", *self.AGENT_NAME)

        self.input_text("+971+test+careerist", *self.PHONE)

        self.input_text("Test", *self.CMPY)

        self.input_text("2024", *self.YR_JOINED)

        self.input_text("cabram1967@comcast.net", *self.CNT_EMAIL)

        self.input_text("English", *self.LANGUAGE)

        self.input_text("00000", *self.LIC_NUM)

        self.input_text("https://www.careerist.com", *self.SOC_MEDIA)
        sleep(3)


    def check_buttons(self):
        close_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CLOSE_BTN))
        save_changes_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SAVE_BTN))


    def right_information_present(self):
        close_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CLOSE_BTN))
        save_changes_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SAVE_BTN))

        assert close_button.is_displayed() and save_changes_button.is_displayed(), "Buttons are not visible or clickable."
        print("Close and Save Changes buttons are present and clickable")
