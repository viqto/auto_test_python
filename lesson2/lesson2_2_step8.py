from selenium import webdriver

import math
import time
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    inputFirst = browser.find_element_by_name("firstname").send_keys("Ivan")

    inputLast = browser.find_element_by_name("lastname").send_keys("Petrov")

    inputEmail = browser.find_element_by_name("email").send_keys("Petrov@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    inputFile = browser.find_element_by_name("file").send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to_alert()
    print(alert.text)

finally:
    time.sleep(10)
    browser.quit()