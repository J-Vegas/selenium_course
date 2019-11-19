from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


def test_button_add_to_basket_on_the_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    WebDriverWait(browser, 10).until(
        expected_conditions.element_to_be_clickable((By.TAG_NAME, 'button')))

    buttons = browser.find_elements(By.TAG_NAME, 'button')
    basket_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')

    assert basket_button.text == buttons[2].text, 'Button "Add to basket" is not on page!'