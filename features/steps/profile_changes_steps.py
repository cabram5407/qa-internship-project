# from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when ('Enter some test information in the input fields')
def enter_test_information(context):
    sleep(3)
    context.app.profile_update_page.input_fields()
    sleep(3)


@then('Check the right information is present in the input fields')
def verify_info(context):
    context.app.profile_update_page.right_information_present()


@then('Check “Close” and “Save Changes” buttons are available and clickable')
def close_save_changes(context):
    context.app.profile_update_page.check_buttons()


    # context.driver.close()