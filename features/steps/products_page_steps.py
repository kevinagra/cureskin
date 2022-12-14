from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click on star/reviews near description')
def click_star_review(context):
    context.app.product_page.click_star_review()

@then('Verify the Products header')
def verify_products_header(context):

    PRODUCTS_HEADER = (By.CSS_SELECTOR, ".collection-hero__title")

    def verify_products_header(self):
        self.wait_for_element_appear(*self.SEE_DEALS)

@then('Verify reviews section')
def verify_reviews_section(context):

    CUSTOMER_REVIEWS_HEADER = (By.XPATH, "//h2[normalize-space()='Customer Reviews']")

    def verify_empty_cart(self):
        expected_result = 'Customer Reviews'
        actual_result = self.driver.find_element(*self.CUSTOMER_REVIEWS_HEADER).text
        assert expected_result == actual_result, f'Expected -> {expected_result}, but got -> {actual_result}'

