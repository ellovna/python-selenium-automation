from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



CLICK_INPUT = (By. ID, "nav-cart-count")
CLICK_BTN = ('Click on Cart Icon')
CLICK_RESULT_TEXT = (By.XPATH, "//*[@id='a-page']/div[2]/div[2]/div[1]/div/div[2]/div/div/h1")

#
# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com')


@when('Click on Cart Icon')
def click_amazon(self):
    self.driver.find_element(*CLICK_INPUT).click()

# def click_amazon(context):
    # context.driver.find_element(*CLICK_INPUT).click()
    #context.driver.find_element(*CLICK_BTN)

