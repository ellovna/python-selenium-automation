from selenium.webdriver.common.by import By
from behave import given, when, then, step


SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state-a-text-bold']")
PRODUCT_PRICE = (By. XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_TO_CART_BTN = (By. ID, 'add-to-cart-button')


@when('Click on the first product')
def click_first_product(self):
    self.driver.find_element(*PRODUCT_PRICE).click()


@when('Click on Add to cart button')
def click_on_cart_btn(self, *add_to_cart_btn):
    self.driver.find_element(*ADD_TO_CART_BTN).click()



