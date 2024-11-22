from selenium import webdriver

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from app.application import Application
from support.logger import logger


def browser_init(context, scenario_name):
    """
    :param scenario_name:
    :param context: Behave context
    """

    # context.driver = webdriver.Chrome(service=service, options=chrome_options)





#Mobile Device configuration
    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.implicitly_wait(6)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

#generates test file for Allure
# behave -f allure_behave.formatter:AllureFormatter -o test_results/features/tests/product_page.feature
# allure serve test_results/

#Appium Platform
# appium_server_url = "http://localhost:4723/wd/hub"
# capabilities_options = UiAutomator2Options().loadcapabilities(DesiredCapabilities)
# mobile_Emulation = {"deviceName" : "Pixel 5"}
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#
# driver = webdriver.Remote(appium_server_url, options=capabilities_options)
# driver.implicility.wait(5)


#Google Chrome browser
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

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

def before_scenario(context, scenario):
    # Initialize the Firefox WebDriver before each scenario
    # print('\nStarted scenario: ', scenario.name )
    # browser_init(context, scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        # print('\nStep failed: ', step)
        logger.warning(f'Step failed: {step}')

def after_scenario(context, feature):
    # if context.driver:
        context.driver.quit()

