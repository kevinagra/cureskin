from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from app.application import Application

# Standard mode - PyCharm:
# def browser_init(context):

# With BrowserStack:
def browser_init(context, test_case):

    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path="/Users/Kevin/Documents/Automation/python-selenium-automation/chromedriver")
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox(executable_path="/Users/Kevin/Documents/Automation/cureksin-main/geckodriver")

    # Headless mode, Firefox:
    #     options = webdriver.FirefoxOptions()
    #     options.add_argument('headless')
    #     context.driver = webdriver.Firefox(options=options)

    # Headless mode, Chrome:
    #     options = webdriver.ChromeOptions()
    #     options.add_argument('headless')
    #     context.driver = webdriver.Chrome(chrome_options=options)

# BrowserStack
    desired_cap = {
        'bstack:options': {
            "os": "Windows",
            "osVersion": "11",
            "browserVersion": "latest",
            "projectName": "CureSkin",
            "buildName": "CAP_11_Shop_All.feature",
            "local": "false",
            "networkLogs": "true",
            "seleniumVersion": "3.14.0",
        },
        "browserName": "Chrome",
        'name': test_case
    }

    bs_user = 'kevinagra_4E2DXN'
    bs_key = 'HPm18ZB8PcM1T2nj2R8M'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote (url, desired_capabilities=desired_cap)
    context.app = Application(context.driver)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 5)
    context.app = Application(context.driver)


# Turn off if not using BrowserStack
def before_scenario(context, scenario):
    browser_init(context, scenario.name)


# Standard mode - PyCharm:
# def before_scenario(context, scenario):
#     print('\nStarted scenario: ', scenario.name)
#     browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()


def close_browser(context, step):
    context.driver.close()

