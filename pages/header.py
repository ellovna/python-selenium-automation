from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.XPATH, '//*[@id="nav-orders"]/span[2]')
    FLAG = (By.CSS_SELECTOR, ".icp-nav-flag-us")
    SPANISH_LANG = (By.CSS_SELECTOR, "[href='#switch-lang=es_US']")
    DEPARTMENT_SELECT = (By.ID, "searchDropdownBox")
    DEPARTMENT_SUB_NAV = (By.CSS_SELECTOR, "[data-category='{SUBSTRING}']")

    def get_department_sub_nav_locator(self, department):
        return [self.DEPARTMENT_SUB_NAV[0], self.DEPARTMENT_SUB_NAV[1].replace('{SUBSTRING}', department)]

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def sign_in(self):
        self.click_orders(*self.ORDERS_BTN)

    def hover_lang(self):
        actions = ActionChains(self.driver)
        flag = self.find_element(*self.FLAG)
        actions.move_to_element(flag)
        actions.perform()

    def select_dept(self, alias):
        department_select = self.find_element(*self.DEPARTMENT_SELECT)
        select = Select(department_select)
        select.select_by_value(f'search-alias={alias}')

    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def verify_department(self, department):
        department_locator = self.get_department_sub_nav_locator(department)
        self.wait_for_element_appear(*department_locator)













