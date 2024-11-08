from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

EMAIL = (By.CSS_SELECTOR, "input#email-2.input.w-input")
PSWD = (By.CSS_SELECTOR, "input#password-2.input.w-input")
LOGIN_BTN = (By.CSS_SELECTOR, "a.login-button.w-button")


@given('Open the main page')
def open_reelly_page(context):
    context.driver.get('https://soft.reelly.io')


@when('Log in to the page')
def click_login_button(context, *LOGIN_BTN, EMAIL, PSWD, text):
         context.driver.input_text(EMAIL).send_keys(text)
         context.driver.input_text(PSWD).send_keys(text)
         context.driver.wait_to_be_clickable_click(LOGIN_BTN).click()


