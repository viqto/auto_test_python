from selenium import webdriver

import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#treasure[valuex]")
    print(x_element)
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)
    print(y)

    inputAnswer = browser.find_element_by_id("answer")
    inputAnswer.send_keys(y)

    checkboxR = browser.find_element_by_id("robotCheckbox")
    checkboxR.click()

    radioR = browser.find_element_by_id("robotsRule")
    radioR.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

