from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify the empty cart')
def verify_cart(context):

    EMPTY_CART = (By.XPATH, "//h1[text()='Back to School']")

    def verify_empty_cart(self):
        expected_result = 'Your cart is empty'
        actual_result = self.driver.find_element(*self.EMPTY_CART).text
        assert expected_result == actual_result, f'Expected -> {expected_result}, but got -> {actual_result}'

    # context.app.empty_cart_page.verify_empty_cart()


