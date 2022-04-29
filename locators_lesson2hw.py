import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\Home PC\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://www.amazon.com/')

# Signin
driver.find_element(By. XPATH, "//*[@id='nav-signin-tooltip']/a/span").click()

# Amazon logo
driver.find_element(By. XPATH, "//*[@id='a-page']/div[1]/div[1]/div/a/i")

# Email field
driver.find_element(By. ID, 'ap_email')

# Continue button
driver.find_element(By. XPATH, "//input[@id='continue']")

# Need help link
driver.find_element(By. XPATH, '//a[@class="a-expander-header a-declarative a-expander-inline-header a-link-expander"]').click()

# Forgot your password link
#driver.find_element(By. XPATH, "//*[@id='auth-fpp-link-bottom']").click()

# Other issues with Sign-In link
driver.find_element(By. XPATH, "//*[@id='ap-other-signin-issues-link']").click()

# Create your Amazon account button
driver.find_element(By. XPATH, "//*[@id='createAccountSubmit']").click()

# *Conditions of use link
driver.find_element(By. XPATH, "//*[@id='a-page']/div[1]/div[4]/div[2]/a[1]").click()

# *Privacy Notice link
driver.find_element(By. XPATH, "//*[@id='a-page']/div[1]/div[4]/div[2]/a[2]").click()

time.sleep(2)
driver.quit()