from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#num1").text
    num2 = browser.find_element_by_css_selector("#num2").text

    summ = str(int(num1) + int(num2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summ)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(10)

    browser.quit()
