# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
#
#
# SEARCH_INPUT = (By. ID, "helpsearch")
# SEARCH_BTN = ("Cancel Items")
# SEARCH_RESULT_TEXT = (By.XPATH, "//div[@class='help-content']/h1")
#
#
#
# @given('Open Amazon Help Page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=3')
#
#
#
# @when('Search for {search_word}')
# def search_amazon(context, search_word):
#     context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
#     context.driver.find_element(*SEARCH_INPUT).send_keys(Keys.ENTER)
#


