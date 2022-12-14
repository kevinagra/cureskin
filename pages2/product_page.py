from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pages.base_page import Page

class ProductPage(Page):

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')
    NEW_ARRIVAL_SELECTION = (By.CSS_SELECTOR, "[href='/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6']")
    SEE_DEALS = (By.CSS_SELECTOR, '.mm-merch-panel')
    STAR_REVIEW_LINK = (By.CSS_SELECTOR, ".jdgm-prev-badge__text")

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BUTTON)

    def hover_new_arrivals(self):
        new_arrival_selection = self.find_element(*self.NEW_ARRIVAL_SELECTION)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrival_selection)
        actions.perform()

        sleep(4)

    def click_star_review(self):
        self.click(*self.STAR_REVIEW_LINK)

    def verify_see_deals(self):
        self.wait_for_element_appear(*self.SEE_DEALS)



