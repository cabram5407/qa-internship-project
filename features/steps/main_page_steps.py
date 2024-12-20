from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_reelly_page(context):
    sleep(5)
    context.app.login_page.open_page()
    sleep(5)


@when('Log in to the page')
def click_login_button(context):
    sleep(3)
    context.app.login_page.input_login_information()
    sleep(3)

