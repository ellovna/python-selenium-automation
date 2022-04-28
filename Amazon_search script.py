from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path=r'C:\Users\Home PC\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://www.amazon.com/')
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')

driver.find_element(By. ID, 'nav-search-submit-button').click()

actual_result = '"coffee"'
expected_result = driver.find_element(By. XPATH, "//span[@class='a-color-state a-text-bold']").text
sleep(2)

assert actual_result == expected_result, f'Error! actual text {actual_result} does not match expected {expected_result}'

print("Test case passed")

driver.quit()