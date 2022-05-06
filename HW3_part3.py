from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='/Users/ellaoroz/Desktop/chromedriver')
driver.get('https://www.amazon.com/gp/help/customer/display.html')


search_bar = driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/cart/view.html?ref_=nav_cart']")
search_bar.send_keys("Cart", Keys.ENTER)


actual_result = driver.find_element(By. XPATH, '//*[@id="sc-active-cart"]/div/div/div[2]/div[1]/h2').text
expected_result = 'Your Amazon Cart is empty'
assert actual_result == expected_result, f'Error! actual text {actual_result} does not match expected {expected_result}'

print("Test case passed")

driver.quit()