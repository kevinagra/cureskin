from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from app.application import Application

# Allure commands: (1) run, (2) generate report:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/CAP_72_View_All.feature
# allure serve test_results/

# Standard mode - PyCharm:
def browser_init(context):

# With BrowserStack:
# def browser_init(context, test_case):

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
#     desired_cap = {
#         'bstack:options': {
#             "os": "Windows",
#             "osVersion": "11",
#             "browserVersion": "latest",
#             "projectName": "CureSkin",
#             "buildName": "CAP_72_View_All.feature",
#             "local": "false",
#             "networkLogs": "true",
#             "seleniumVersion": "3.14.0",
#         },
#         "browserName": "Chrome",
#         'name': test_case
#     }
#
#     bs_user = 'kevinagra_4E2DXN'
#     bs_key = 'HPm18ZB8PcM1T2nj2R8M'
#     url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#     context.driver = webdriver.Remote (url, desired_capabilities=desired_cap)
#     context.app = Application(context.driver)


# Miscellaneous Configs
    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 5)
    context.app = Application(context.driver)


# Mobile Test
mobile_emulation = {
   "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
   "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options = chrome_options)


# Turn off if not using BrowserStack
# def before_scenario(context, scenario):
#     browser_init(context, scenario.name)


# Standard mode - PyCharm:
def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


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

