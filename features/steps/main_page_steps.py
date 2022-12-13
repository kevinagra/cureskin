from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open CureSkin page')
def open_cureskin(context):
    context.app.main_page.open_main()

@when('Click on cart icon')
def click_cart(context):
    context.app.main_page.click_cart_icon()

@when('Click on Shop All button')
def shop_all_BTN(context):
    context.app.main_page.click_shop_all()




