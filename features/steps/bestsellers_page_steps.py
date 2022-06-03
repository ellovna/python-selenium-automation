from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


TOP_LINKS = (By. CSS_SELECTOR, '#zg_header a')
HEADER = (By. CSS_SELECTOR, '#zg_banner_text')
BEST_S_BTN = (By. CSS_SELECTOR, 'a[href*="/Best-Sellers/zgbs/ref=zg_bs_tab"]')
NEW_RELEASES_BTN = (By. CSS_SELECTOR, 'a[href*="/gp/new-releases/ref=zg_bs_tab"]')
MOVERS_SHAKERS_BTN = (By. CSS_SELECTOR, 'a[href*="/gp/movers-and-shakers/ref=zg_bsnr_tab"]')
MOST_WISHED_FOR_BTN = (By. CSS_SELECTOR, 'a[href="/gp/most-wished-for/ref=zg_bsms_tab"]')
GIFT_IDEAS_BTN = (By. CSS_SELECTOR, 'a[href*="/gp/most-gifted/ref=zg_mw_tab"]')
# TOP_LINKS = (By.CSS_SELECTOR, "#CardInstancebEE_l87YctXw03PpM_3rZg")
top_links = (By. CSS_SELECTOR, 'a[href*="/Best-Sellers/zgbs/ref=zg_bs_tab"]'), (By. CSS_SELECTOR, 'a[href*="/gp/new-releases/ref=zg_bs_tab"]'), (By. CSS_SELECTOR, 'a[href*="/gp/movers-and-shakers/ref=zg_bsnr_tab"]'), (By. CSS_SELECTOR, 'a[href="/gp/most-wished-for/ref=zg_bsms_tab"]'), (By. CSS_SELECTOR, 'a[href*="/gp/most-gifted/ref=zg_mw_tab"]')


@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    context.driver.get('http://www.amazon.com/gp/bestsellers/')


# @then('Verify there are {expected_links} links')
# def verify_link_count(context, expected_links):
#     actual_links = context.driver.find_elements(*TOP_LINKS)
#     assert len(actual_links) == int(expected_links), f' Expected {expected_links} links, but but got {len(expected_links)}'


@when('Click on BestSellers button')
def click_bs_btn(context):
    context.driver.find_element(*BEST_S_BTN).click()


@when('Click on New Releases button')
def click_new_r_btn(context):
    context.driver.find_element(*NEW_RELEASES_BTN).click()


@when('Click on Movers&Shakers button')
def click_movers_and_shakers_btn(context):
    context.driver.find_element(*MOVERS_SHAKERS_BTN).click()


@when('Click on Most Wished For button')
def click_most_wished_for_btn(context):
    context.driver.find_element(*MOST_WISHED_FOR_BTN).click()


@when('Click on Gift Ideas')
def click_on_gift_ideas_btn(context):
    context.driver.find_element(*GIFT_IDEAS_BTN).click()


# @then('Verify user sees "Amazon Best Sellers" text')
# def user_sees_text(context):
#     context.driver.find_element(*HEADER)
#
#
# @then('Verify user sees "Amazon Hot New Releases" text')
# def user_sees_text(context):
#     context.driver.find_element(*HEADER)


@then('Verify user sees {text} text')
def user_sees_text(context, text):
    context.driver.find_element(*HEADER)


    for x in range(len(top_links)):
        link_to_click = context.driver.find_elements(*TOP_LINKS)[x]
        link_text = link_to_click.text
        link_to_click.click()
        sleep(1)
        new_text = context.driver.find_element(*HEADER).text
        assert link_text in new_text, f'Expected {link_text} to be in {header_text}'


