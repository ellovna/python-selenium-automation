from selenium.webdriver.common.by import By
from behave import given, when, then, step


SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state-a-text-bold']")
PRODUCT_PRICE = (By. XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_TO_CART_BTN = (By. ID, 'add-to-cart-button')


@when('Click on the first product')
def click_first_product(context):
    context.app.product_page.click_first_product()


@when('Click on Add to cart button')
def click_on_cart_btn(context):
    context.app.product_page.add_to_cart_button()
