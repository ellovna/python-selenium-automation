from pages.base_page import Page

from selenium.webdriver.common.by import By


class SignInPage(Page):
    SIGN_IN_P = (By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[1]/form/div/div/div/h1')

    def verify_sign_in_page_opened(self):
        self.driver.find_element(*self.SIGN_IN_P)
