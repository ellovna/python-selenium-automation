from pages.bestsellers_page import BestsellersPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.cart_page import AmazonCart
from pages.product_page import ProductPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.bestsellers_page = BestsellersPage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.cart_page = AmazonCart(self.driver)
        self.product_page = ProductPage(self.driver)




# a = Application()
# a.header.search_amazon()
# a.main_page.open_main_page()

