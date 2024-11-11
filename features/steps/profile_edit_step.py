from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Edit profile option')
def edit_profile(context):
    context.app.profile_edits_page.profile_edit()
    sleep(3)
