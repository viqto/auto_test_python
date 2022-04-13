from selenium.webdriver.support.ui import Select
from selenium import webdriver

import math
import time


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    x = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    y = int(num2.text)
    z = str(x + y)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(z)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to_alert()
    print(alert.text)

finally:
    time.sleep(5)
    browser.quit()

