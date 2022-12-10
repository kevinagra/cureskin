from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.empty_cart_page import EmptyCartPage
from pages.results_page import ResultsPage
from pages.product_page import ProductPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.empty_cart_page = EmptyCartPage(self.driver)
        self.results_page = ResultsPage(self.driver)
        self.product_page = ProductPage(self.driver)


