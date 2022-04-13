from telnetlib import EC

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element_by_id("book")
    button.click()

    browser.execute_script("window.scrollBy(0, 200);")

    x_element = browser.find_element_by_css_selector("label>:nth-child(2)")
    x = x_element.text
    y = calc(x)

    inputAnswer = browser.find_element_by_id("answer")
    inputAnswer.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()
