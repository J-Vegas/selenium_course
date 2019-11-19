import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('steps', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1",
                                    "236899/step/1", "236903/step/1", "236904/step/1", "236905/step/1"])
def test_get_to_steps(browser, steps):
    link = f"https://stepik.org/lesson/{steps}/"
    browser.get(link)
    input = browser.find_element_by_css_selector("div textarea")
    input.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    answer = browser.find_element_by_css_selector("div pre").text
    assert "Correct!" == answer
