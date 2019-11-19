from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        in1 = browser.find_element(By.XPATH, '//input[@class="form-control first"][@required]')
        in1.send_keys("First")
        in2 = browser.find_element(By.XPATH, '//input[@class="form-control second"][@required]')
        in2.send_keys("Last")
        in3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        in3.send_keys("Email")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        time.sleep(1)
        browser.quit()

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        in1 = browser.find_element(By.XPATH, '//input[@class="form-control first"][@required]')
        in1.send_keys("First")
        in2 = browser.find_element(By.XPATH, '//input[@class="form-control second"][@required]')
        in2.send_keys("Last")
        in3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        in3.send_keys("Email")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(1)
        browser.quit()

if __name__ == "__main__":
    unittest.main()
