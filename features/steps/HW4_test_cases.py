from selenium.webdriver.common.by import By
from behave import given, when, then, step
from time import sleep

# Test case #1
# BESTSELLERS_LINKS = (By. CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR')

#
# @given('Open Amazon BestSellers page')
# def open_amazon_bestsellers_page(context):
#     context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
#
#
#
# @then('Verify there are {expected_amount} BestSellers links')
# def verify_tab_links_count(context, expected_amount):
#     expected_amount = int(expected_amount)
#     tab_links = context.driver.find_elements(*BESTSELLERS_LINKS)
#     assert len(tab_links) == expected_amount, f'Expected {expected_amount} links, but got {len(bestsellers_links)}'
#



#Test case #3

ISSUECARD_LINKS = (By. CSS_SELECTOR, 'div.issue-card-wrapper')
HELPTOPIC_LINKS = (By. CSS_SELECTOR, 'li.help-topics')


@given('Open Amazon Customer Service page')
def open_amazon_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/hz/contact-us/foresight/hubgateway')



@then('Verify there are {expected_amount} Issue Card wrapper links')
def verify_issuecard_links_count(context, expected_amount):
    expected_amount = int(expected_amount)
    issuecard_links = context.driver.find_elements(*ISSUECARD_LINKS)
    assert len(issuecard_links) == expected_amount, f'Expected {expected_amount} links, but got {len(issuecard_links)}'


@then('Verify there are {expected_amount} Help Topics links')
def verify_helptopic_links_count(context, expected_amount):
    expected_amount = int(expected_amount)
    helptopic_links = context.driver.find_elements(*HELPTOPIC_LINKS)
    assert len(helptopic_links) == expected_amount, f'Expected {expected_amount} links, but got {len(helptopic_links)}'
