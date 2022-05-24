from selenium.webdriver.common.by import By
from behave import when, given, then, step
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


ADD_TO_CART_BTN = (By. ID, 'add-to-cart-button')
# SEARCH_INPUT = (By. ID, 'twotabsearchtextbox')
# SEARCH_BTN = (By.ID, 'nav-search-submit-button')
PRODUCT_NAME = (By. ID, 'productTitle')
# COLOR_OPTIONS = (By. CSS_SELECTOR, "#inline-twister-expander-content-color_name li[class*='desktop']")
COLOR_NAME = (By. ID, 'inline-twister-expanded-dimension-text-color_name')
COLOR_OPTIONS = (By. CSS_SELECTOR, "#inline-twister-row-color_name li[class*='slots']")
COLOR = (By. CSS_SELECTOR, "#color_name_8-announce")


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


# @then('Verify user can click through colors')
# def verify_clicking_colors(context):
#     expected_colors = ['Navy', 'Black', 'Solid Black', 'Multicolour']
#     actual_colors = []
#
#     color_options = context.driver.find_elements(*COLOR_OPTIONS)
#     for option in color_options:
#         option.click()
#         sleep(2)
#         color_name = context.driver.find_element(*COLOR_NAME).text
#         actual_colors += [color_name]
#
#     assert actual_colors == expected_colors, f'Error! Expected {expected_colors}, but got {actual_colors}'


@then('Verify user can click through colors')
def verify_clicking_colors(context):
    expected_colors = ['Army Green', 'Army Green-1', 'Black', 'Black-1', 'Blue', 'Brick Red', 'Green', 'Lavender-1', 'Light Pink', 'Light Purple', 'Navy', 'Sky Blue-1', 'White', 'White-1', 'Yellow', 'Yellow-1']
    actual_colors = []

    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for option in color_options:
        option.click()
        sleep(4)
        color_name = context.driver.find_element(*COLOR_NAME).text
        actual_colors += [color_name]

    assert actual_colors == expected_colors, f'Error! Expected {expected_colors}, but got {actual_colors}'

