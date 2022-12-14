from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

class MainPage(Page):

    CART_ICON = (By.CSS_SELECTOR, ".icon.icon-cart-empty")
    SHOP_ALL_BTN = (By.XPATH, "//span[normalize-space()='Shop All']")
    CLICK_PRODUCT = (By.XPATH, "//a[normalize-space()='CureSkin Broad Spectrum Sunscreen - SPF 30']")

    def open_main(self):
        self.driver.get("https://shop.cureskin.com/")

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def click_shop_all(self):
        self.click(*self.SHOP_ALL_BTN)

    def click_product(self):
        self.click(*self.CLICK_PRODUCT)

