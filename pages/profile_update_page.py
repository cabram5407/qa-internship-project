from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from time import sleep


class ProfileUpdatePage(Page):
    AGENT_NAME = (By.ID, "Fullname")
    PHONE = (By.ID, "number")
    CMPY = (By.ID, "Company-name")
    YR_JOINED = (By.ID, "When-joined-company-2")
    CNT_EMAIL = (By.ID, "Email-2")
    LANGUAGE = (By.ID, "Languages")
    LIC_NUM = (By.ID, "When-joined-company")
    SOC_MEDIA = (By.ID, "Email")

    SAVE_BTN = (By.XPATH, "//div[@class='save-changes-button']")
    CLOSE_BTN = (By.CSS_SELECTOR, "a.close-button.w-button")


    def input_fields(self):
        self.input_text("", *self.AGENT_NAME)
        self.input_text("", *self.PHONE)
        self.input_text("", *self.CMPY)
        self.input_text("", *self.YR_JOINED)
        self.input_text("", *self.CNT_EMAIL)
        self.input_text("", *self.LANGUAGE)
        self.input_text("", *self.LIC_NUM)
        self.input_text("", *self.SOC_MEDIA)
        sleep(3)


    def right_information_present(self):
        name_field = self.find_element(*self.AGENT_NAME)
        actual_full_name = name_field.get_attribute("value")
        expected_full_name = "test+Charmaine Abram+careerist"
        assert actual_full_name == expected_full_name, f"Expected {expected_full_name} but got {actual_full_name}"

        # phone_field = self.find_element(*self.PHONE)
        # actual_phone = phone_field.get_attribute("value")
        # expected_phone = "+971+test+careerist"
        # assert actual_phone == expected_phone, f"Expected {expected_phone} but got {actual_phone}"
        #
        # company_field = self.find_element(*self.CMPY)
        # actual_company = company_field.get_attribute("value")
        # expected_company = "Test"
        # assert actual_company == expected_company, f"Expected {expected_company} but got {actual_company}"
        #
        # year_joined = self.find_element(*self.YR_JOINED)
        # actual_year = year_joined.get_attribute("value")
        # expected_year = "2024"
        # assert actual_year == expected_year, f"Expected {expected_year} but got {actual_year}"
        #
        # company_email = self.find_element(*self.CNT_EMAIL)
        # actual_email = company_email.get_attribute("value")
        # expected_email = "cabram1967@comcast.net"
        # assert actual_email == expected_email, f"Expected {expected_email} but got {actual_email}"
        #
        # language_field = self.find_element(*self.LANGUAGE)
        # actual_language = language_field.get_attribute("value")
        # expected_language = "English"
        # assert actual_language == expected_language, f"Expected {expected_language} but got {actual_language}"
        #
        # license_field = self.find_element(*self.LIC_NUM)
        # actual_license = license_field.get_attribute("value")
        # expected_license = "00000"
        # assert actual_license == expected_license, f"Expected {expected_license} but got {actual_license}"
        #
        # media_field = self.find_element(*self.SOC_MEDIA)
        # actual_media = media_field.get_attribute("value")
        # expected_media = "https://www.careerist.com"
        # assert actual_media == expected_media, f"Expected {expected_media} but got {actual_media}"


    def check_buttons(self):
        save_changes_button = self.find_elements(*self.SAVE_BTN)
        close_button = self.find_elements(*self.CLOSE_BTN)

        save_changes_button_final = save_changes_button[1].text
        close_button_final = close_button[1].text

        assert save_changes_button_final == 'Save changes', f'Save changes button {save_changes_button_final} was not found.'
        assert close_button_final == 'Close', f'Close button {close_button_final} was not found.'

        print("Close and Save Changes buttons are present and clickable")
