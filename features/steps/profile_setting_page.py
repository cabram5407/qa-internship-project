# from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on settings option')
def user_setting(context):
    sleep(5)
    context.app.profile_setting_page.navigate_to_setting()

