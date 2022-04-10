from selenium import webdriver

import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("label>:nth-child(2)")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    inputAnswer = browser.find_element_by_id("answer")
    inputAnswer.send_keys(y)

    checkboxR = browser.find_element_by_id("robotCheckbox")
    checkboxR.click()

    radioR = browser.find_element_by_id("robotsRule")
    radioR.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to_alert()
    print(alert.text)

finally:
    time.sleep(10)
    browser.quit()