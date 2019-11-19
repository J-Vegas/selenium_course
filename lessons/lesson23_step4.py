from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    browser.find_element_by_css_selector('.btn').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element_by_css_selector("#input_value").text)
    y = calc(x)

    in_answer = browser.find_element_by_css_selector('#answer').send_keys(y)

    browser.find_element_by_css_selector('.btn').click()

finally:

    time.sleep(10)

    browser.quit()
