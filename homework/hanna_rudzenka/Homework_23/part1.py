import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    driver = Chrome()
    yield driver


def test_submitted_element(browser):
    browser.get('https://www.qa-practice.com/elements/input/simple')
    text_string = browser.find_element(By.NAME, "text_string")
    text_string.send_keys("potato")
    text_string.submit()
    result_text = browser.find_element(By.CLASS_NAME, "result-text").text
    print(result_text)
