import unittest
import  time
from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"
linkFail = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(linkFail)


class TestReg(unittest.TestCase):

    def test_case1(self):
        name = browser.find_element_by_css_selector("div.first_block>div>input").send_keys("Ivan")
        self.assertEqual(name, name, "Should be absolute value of a number")

    def test_case2(self):
        last_name = browser.find_element_by_css_selector("div.first_block>div.second_class>input").send_keys("Petrov")
        self.assertEqual(last_name, last_name, "Should be absolute value of a number")

    def test_case3(self):
        input3 = browser.find_element_by_css_selector("div.first_block>div.third_class>input").send_keys("Petrov@gmail.com")

    def test_case4(self):
        input4 = browser.find_element_by_css_selector("div.second_block>div>input").send_keys("+79123456789")

    def test_case5(self):
        input5 = browser.find_element_by_css_selector("div.second_block>div.second_class>input").send_keys("Russia")

    def test_case6(self):
        button = browser.find_element_by_css_selector("button.btn").click()

    def test_case7(self):
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        text = 'Congratulations! You have successfully registered!'
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(str(text), welcome_text, "Не проходит")

    # # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(30)
    # # закрываем браузер после всех манипуляций
    # browser.quit()


if __name__ == "__main__":
    pytest.main()

