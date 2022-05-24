from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from time import sleep



SEARCH_INPUT = (By. ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
#SEARCH_RESULT_TEXT = (By. XPATH, '//*[@id="search"]/span/div/h1/div/div[1]/div/div/span[3]')
#HAM_MENU_BTN = (By. ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By. CSS_SELECTOR, 'td.navFooterDescItem a')
SIGN_IN_BTN = (By. CSS_SELECTOR, '#nav-signin-tooltip .nav-action-inner')
SEARCH_RESULTS = (By. CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By. CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By. CSS_SELECTOR, 'img[data-image-latency="s-product-image"]')


@given("Open Amazon page")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')



@when("Search for {search_word}")
def search_amazon(context, search_word):
     context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
     context.driver.find_element(*SEARCH_BTN).click()

#
# @when('Click on button from SignIn popup')
# def click_sign_in_btn(context):
#     context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable').click()

#
# @then('Verify search results for {expected_result} is shown')
# def verify_search_results(context, expected_result):
#     actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT).text
#     assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match {expected_result}'
#

# @then('Verify hamburger menu btn present')
# def verify_ham_menu(context):
#     elements = context.driver.find_elements(*HAM_MENU_BTN)
#     assert len(elements) == 1, f'Error: Expected 1 item, but got {len(elements)}'

#
# @then('Verify hamburger menu btn present')
# def verify_ham_menu(context):
#     context.driver.find_element(*HAM_MENU_BTN)


#
# @then('Verify there are {expected_amount} footer links')
# def verify_footer_links_count(context, expected_amount):
#     expected_amount = int(expected_amount)
#     footer_links = context.driver.find_elements(*FOOTER_LINKS)
#     assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'
#


@then('Verify that every product has a name and image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title != '', 'Error! Title should not be blank'
        print(title)

        product.find_element(*PRODUCT_IMG)





