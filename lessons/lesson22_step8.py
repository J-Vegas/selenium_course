from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    input1 = browser.find_element_by_xpath('//input[@name="firstname"]').send_keys("First")
    input2 = browser.find_element_by_xpath('//input[@name="lastname"]').send_keys("Last")
    input3 = browser.find_element_by_xpath('//input[@name="email"]').send_keys("Email")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'hello.txt')
    browser.find_element_by_css_selector('#file').send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:

    time.sleep(10)

    browser.quit()
