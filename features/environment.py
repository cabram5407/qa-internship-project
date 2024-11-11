from lib2to3.fixes.fix_input import context

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """

#Google Chrome browser
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.implicitly_wait(6)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


#Firefox browser
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)


######HEADLESS Chrome handling for test script#######
options = webdriver.ChromeOptions()
options.add_argument('headless')
service=Service(ChromeDriverManager().install())
context.driver = webdriver.Chrome(
    options=options,
    service=service
)

def before_scenario(context, scenario):
    # Initialize the Firefox WebDriver before each scenario
    context.driver = webdriver.Firefox()

    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    if context.driver:
        context.driver.quit()

