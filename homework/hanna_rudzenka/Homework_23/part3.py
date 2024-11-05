import time
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def browser():
    driver = Chrome()
    yield driver


def test_result_text(browser):
    browser.get("https://www.qa-practice.com/elements/select/single_select")
    browser.find_element(By.CLASS_NAME, "form-select").click()
    Select(browser.find_element(By.CLASS_NAME, "form-select")).select_by_visible_text("Ruby")
    browser.find_element(By.ID, "submit-id-submit").click()
    result_text = browser.find_element(By.CLASS_NAME, "result-text").text
    assert result_text == 'Ruby'


def test_hello_world_text(browser):
    browser.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    browser.find_element(By.TAG_NAME, "button").click()
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#finish'))).is_displayed()
