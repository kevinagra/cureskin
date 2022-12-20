from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    # context.driver = webdriver.Chrome(executable_path="/Users/Kevin/Documents/Automation/python-selenium-automation/chromedriver")
    # context.driver = webdriver.Safari()
    context.driver = webdriver.Firefox(executable_path="/Users/Kevin/Documents/Automation/cureksin-main/geckodriver")

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 5)
    context.app = Application(context.driver)


# Headless mode, Firefox:
    options = webdriver.FirefoxOptions()
    options.add_argument('headless')
    context.driver = webdriver.Firefox(options=options)

# Headless mode, Chrome:
#     options = webdriver.ChromeOptions()
#     options.add_argument('headless')
#     context.driver = webdriver.Chrome(chrome_options=options)


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


def close_browser(context,step):
    context.driver.close()

