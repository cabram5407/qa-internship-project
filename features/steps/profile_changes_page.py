from PIL.TiffImagePlugin import SAVE_INFO
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

AGNT_NAME = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='Fullname']")
PHONE = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='number']")
CMPY = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='Company name']")
YR_JOINED = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='When Joined Company 2']")
CNT_EMAIL = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='Email 2']")
LANGUAGE = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='Languages']")
LIC_NUM = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='When joined company']")
SOC_MEDIA = (By.CSS_SELECTOR, "input.field-form-block.w-input[data-name='Email']")

SAVE_BTN = (By.CSS_SELECTOR, "div.save-changes-button[wized='saveButtonProfile']")
CLOSE_BTN = (By.CSS_SELECTOR, "a.close-button.w-button[href='/settings']")


@when ('Enter some test information in the input fields')
def input_fields(context, *AGNT_NAME, PHONE, CMPY, YR_JOINED, CNT_EMAIL, LANGUAGE, LIC_NUM, SOC_MEDIA, text):
    context.driver.find_element(AGNT_NAME).send_keys(text)
    context.driver.find_element(PHONE).send_keys(text)
    context.driver.find_element(CMPY).send_keys(text)
    context.driver.find_element(YR_JOINED).send_keys(text)
    context.driver.find_element(CNT_EMAIL).send_keys(text)
    context.driver.find_element(LANGUAGE).send_keys(text)
    context.driver.find_element(LIC_NUM).send_keys(text)
    context.driver.find_element(SOC_MEDIA).send_keys(text)


@then('Check the right information is present in the input fields')
def verify_right_info(context, locator, expected_text):
    actual_text = context.find_element(*locator).text
    assert actual_text == expected_text, f'Expected {expected_text}, did not match {actual_text}'


@then('Check “Close” and “Save Changes” buttons are available and clickable')
def close_save_changes(context, *SAVE_BTN, CLOSE_BTN):
    context.driver.wait_to_be_clickable_click(SAVE_BTN).click()
    context.driver.wait_to_be_clickable_click(CLOSE_BTN).click()
