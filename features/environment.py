from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from app.application import Application
# from support.logger import logger

def browser_init(context):
    # """
    # :param context: Behave context
    # """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


# def before_scenario(context, scenario):
#     # print('\nStarted scenario: ', scenario.name)
#     logger.info(f'\nStarted scenario: {scenario.name}')
#     browser_init(context, scenario.name)


# def before_step(context, step):
#     # print('\nStarted step: ', step)
#     logger.info(f'\nStarted step: {step}')


# def after_step(context, step):
#     if step.status == 'failed':
#         # print('\nStep failed: ', step)
#         logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.quit()
