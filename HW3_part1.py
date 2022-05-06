from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='Users/ellaoroz/Desktop/chromedriver')
driver.get('https://www.amazon.com/')

# Amazon logo
driver.find_element(By. CSS_SELECTOR, '.a-icon-logo')

# Create account
driver.find_element(By. XPATH, '//*[@id="ap_register_form"]/div/div/h1')
driver.find_element(By. CSS_SELECTOR, "h1[class='a-spacing-small']")

# Your name label
driver.find_element(By. CSS_SELECTOR, "label[for='ap_customer_name']")

# First and last name
driver.find_element(By. CSS_SELECTOR, "input#First and last name")

# Mobile number or email label
driver.find_element(By. CSS_SELECTOR, "label[for='ap_email']")

# Mobile or email
driver.find_element(By. CSS_SELECTOR, "input#ap_email")

# Password label
driver.find_element(By. CSS_SELECTOR, "label[for='ap_password']")

# Password
driver.find_element(By. CSS_SELECTOR, "input#ap_password")

# Re-enter password label
driver.find_elements(By. CSS_SELECTOR, "label[for='ap_password_check']")

# Re-enter password
driver.find_element(By. CSS_SELECTOR, "input#ap_password_check")

# Continue button
driver.find_element(By. CSS_SELECTOR, "input#continue")

# Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

# Privacy Notice
driver.find_element(By. CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

# Already have an account? Sign In label
driver.find_element(By. CSS_SELECTOR, "a[class='a-link-emphasis']")
