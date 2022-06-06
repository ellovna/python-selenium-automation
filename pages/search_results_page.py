from pages.base_page import Page

from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULT_TEXT = (By. XPATH, '//span[@class="a-color-state a-text-bold"]')

    def verify_search_results(self, expected_result):
        self.verify_text(expected_result, *self.SEARCH_RESULT_TEXT)
        # actual_result = self.driver.find_element(*self.SEARCH_RESULT_TEXT).text
        # assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match {expected_result}'
