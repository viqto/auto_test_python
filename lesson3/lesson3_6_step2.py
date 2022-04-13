import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage():

    @pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_first_link(self, browser, link):
        answer = math.log(int(time.time() - 1))
        browser.get(f"https://stepik.org/lesson/{link}/step/1")
        browser.find_element(by=By.CSS_SELECTOR, value="div.quiz-component>textarea").send_keys(answer)
        browser.find_element(by=By.CSS_SELECTOR, value=".submit-submission").click()
        text1 = browser.find_element(by=By.CSS_SELECTOR, value="pre.smart-hints__hint").text
        assert text1 == "Correct!", f"{text1} - не подходит!!!"
