from selenium import webdriver

import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("label>:nth-child(2)")
    x = x_element.text
    y = calc(x)

    inputAnswer = browser.find_element_by_id("answer")
    inputAnswer.send_keys(y)

    checkboxR = browser.find_element_by_id("robotCheckbox")
    checkboxR.click()

    radioR = browser.find_element_by_id("robotsRule")
    radioR.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

