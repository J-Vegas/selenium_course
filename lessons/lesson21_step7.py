from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    gift = browser.find_element_by_css_selector("#treasure")
    x_element = gift.get_attribute('valuex')
    y = calc(x_element)

    in_answer = browser.find_element_by_css_selector('#answer')
    in_answer.send_keys(y)

    on_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    on_checkbox.click()

    on_radio = browser.find_element_by_css_selector('#robotsRule')
    on_radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
