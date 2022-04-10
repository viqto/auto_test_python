from selenium import webdriver

import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)

    x_element = browser.find_element_by_css_selector("label>:nth-child(2)")
    x = x_element.text
    y = calc(x)

    inputAnswer = browser.find_element_by_id("answer")
    inputAnswer.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    time.sleep(1)
    browser.quit()

