from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element_by_css_selector('button.trollface').click()

    new = browser.window_handles[1]
    browser.switch_to.window(new)


    x = int(browser.find_element_by_css_selector("#input_value").text)
    y = calc(x)

    in_answer = browser.find_element_by_css_selector('#answer').send_keys(y)

    browser.find_element_by_css_selector('.btn').click()

finally:

    time.sleep(10)

    browser.quit()
