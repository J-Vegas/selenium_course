from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get('http://SunInJuly.github.io/execute_script.html')

    x = int(browser.find_element_by_css_selector("#input_value").text)
    y = calc(x)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    in_answer = browser.find_element_by_css_selector('#answer').send_keys(y)

    for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
        browser.find_element_by_css_selector(selector).click()

finally:

    time.sleep(10)

    browser.quit()
