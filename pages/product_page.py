from pages.base_page import Page

from selenium.webdriver.common.by import By


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

    def add_to_cart_button(self):
        self.click(*self.ADD_TO_CART_BTN)

    def click_first_product(self):
        self.click(*self.PRODUCT_PRICE)