from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SETTING_BTN = (By.CSS_SELECTOR, "a.menu-button-block.w-inline-block.w--current")
EDIT_PROF = (By.CSS_SELECTOR, "a[href='/profile-edit'].page-setting-block.w-inline-block")

@when('Click on settings option')
def setting_page(context, *SETTING_BTN):
    context.driver.wait_to_be_clickable_click(SETTING_BTN).click()


@when('Click on Edit profile option')
def edit_profile(context, *EDIT_PROF):
    context.driver.wait_to_be_clickable_click(EDIT_PROF).click()