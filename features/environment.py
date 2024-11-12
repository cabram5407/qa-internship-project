# from lib2to3.fixes.fix_input import context

# from allure_behave.utils import scenario_name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


from app.application import Application


def browser_init(context, scenario_name):
    """
    :param scenario_name:
    :param context: Behave context
    """

#Google Chrome browser
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)


#Firefox browser
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)


######HEADLESS Chrome handling for test script#######
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# service=Service(ChromeDriverManager().install())
# context.driver = webdriver.Chrome(
#     options=options,
#     service=service
# )

### BROWSERSTACK###
    # bs_user = 'cabram_QOlckx'
    # bs_key = 'R5JsgqmmDT2xygxz8qyM'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "Windows",
    #     "osVersion": "11",
    #     'browserName': 'chrome',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.implicitly_wait(6)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    # Initialize the Firefox WebDriver before each scenario
    print('\nStarted scenario: ', scenario.name )
    # browser_init(context, scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    # if context.driver:
        context.driver.quit()

