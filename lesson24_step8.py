from selenium import webdriver
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('http://suninjuly.github.io/explicit_wait2.html')

button = WebDriverWait(browser, 15).until(
       EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
browser.find_element_by_css_selector('.btn').click()

x = int(browser.find_element_by_css_selector("#input_value").text)
y = calc(x)
in_answer = browser.find_element_by_css_selector('#answer').send_keys(y)
browser.find_element_by_css_selector('#solve').click()

time.sleep(10)
browser.quit()
