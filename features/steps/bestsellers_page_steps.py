from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep

TOP_LINKS = (By. CSS_SELECTOR, '#zg_header a')
HEADER = (By. CSS_SELECTOR, '#zg_banner_text')

@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    context.driver.get('http://www.amazon.com/gp/bestsellers/')


@then('Verify there are {expected_links} links')
def verify_link_count(context, expected_links):
    actual_links = context.driver.find_elements(*TOP_LINKS)
    assert len(actual_links) == int(expected_links), f' Expected {expected_links} links, but but got {len(expected_links)}'