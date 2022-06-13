from pages.base_page import Page

from selenium.webdriver.common.by import By


class AmazonCart(Page):
    CART_TEXT = (By.XPATH, '//*[@id="sc-active-cart"]/div/div/div[2]/div[1]/h2')
    CART = (By.ID, 'nav-cart-count')

    def amazon_cart(self):
        self.click_orders(*self.CART_TEXT)

    def cart_count(self):
        self.driver.find_element(*self.CART)




