from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/Users/ellaoroz/Desktop/chromedriver')
driver.get('https://www.amazon.com/gp/help/customer/display.html')


search_bar = driver.find_element(By.ID, "helpsearch")
search_bar.send_keys("Cancel Items")
search_bar.send_keys(Keys.ENTER)

actual_result = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
# actual_result = driver.find_element(By. XPATH, "//*[@id='hubHelpSearchInput']").text
expected_result = 'Cancel Items or Orders'


sleep(2)

assert expected_result in actual_result, f'Error! {actual_result} does not match expected {expected_result}'

print('Test case passed')

driver.quit()

## Test case #2
#
# driver = webdriver.Chrome(executable_path=r'C:\Users\Home PC\Downloads\chromedriver_win32\chromedriver.exe')
# driver.get('https://www.amazon.com')
# driver.find_element(By. ID, 'nav-orders').click()
#
# actual_result = driver.find_element(By. XPATH, "//h1[@class='a-spacing-small']").text
# print(actual_result)
# expected_result = "Sign-In"
#
#
# assert actual_result == expected_result, f'Error! actual text {actual_result} does not match expected {expected_result}'
# print("Test case passed")
#
# sleep(3)
#
# driver.quit()
