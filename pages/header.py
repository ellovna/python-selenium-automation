from pages.base_page import Page

from selenium.webdriver.common.by import By


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.XPATH, '//*[@id="nav-orders"]/span[2]')

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def sign_in(self):
        self.click_orders(*self.ORDERS_BTN)










