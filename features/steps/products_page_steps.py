from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify the Products header')
def verify_products_header(context):

    PRODUCTS_HEADER = (By.CSS_SELECTOR, ".collection-hero__title")

    def verify_products_header(self):
        self.wait_for_element_appear(*self.SEE_DEALS)
