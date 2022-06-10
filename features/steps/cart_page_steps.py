from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep


CART = (By. ID, 'nav-cart-count')
PRODUCT_NAME = (By. CSS_SELECTOR, "#sc-active-cart li")
CART_TEXT = (By. XPATH, '//*[@id="sc-active-cart"]/div/div/div[2]/div[1]/h2')


@when('Open cart page')
def open_cart_page(self):
    self.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
    # context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


# @then("Verify 'Your Amazon Cart is empty' text present")
# def amazon_cart(self):
#     self.driver.find_element(*CART_TEXT)
# def amazon_cart(context):
#     context.driver.get(*CART_TEXT)


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name