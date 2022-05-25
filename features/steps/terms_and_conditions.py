from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


PRIVACY_NOTICE_BTN = (By. XPATH, '//*[@id="a-page"]/div[2]/div[2]/div[1]/div[1]/div[3]/p[8]/a')


@given('Open Amazon T&C page')
def open_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=508088&ref_=footer_cou')



@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    print(context.driver.current_window_handle)


@when('Click on Amazon Privacy Notice link')
def amazon_privacy_notice(context):
    context.driver.find_element(*PRIVACY_NOTICE_BTN).click()



@when('Switch to newly opened window')
def switch_to_new_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print("\nAfter click, windows:", context.driver.window_handles)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))


@then('User can close new window and switch back to original')
def switch_back_to_original(context):
    context.driver.switch_to.window(context.original_window)
    context.driver.close()

