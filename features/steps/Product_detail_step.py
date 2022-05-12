from selenium.webdriver.common.by import By
from behave import when, given, then, step
from time import sleep


ADD_TO_CART_BTN = (By. ID, 'add-to-cart-button')
SEARCH_INPUT = (By. ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')



@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(1)

