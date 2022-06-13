from selenium.webdriver.common.by import By
from behave import given, when, then


CLICK_RESULT_TEXT = (By. XPATH, '//*[@id="sc-item-Cae704e96-c616-420c-9635-499697384c50"]')


@then('Verify Click results for {expected_result} are shown')
def verify_click_results(self, expected_result):
    actual_result = self.driver.find_element(*CLICK_RESULT_TEXT).text
    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match {expected_result}'


