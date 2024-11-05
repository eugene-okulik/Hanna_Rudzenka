import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--force-device-scale-factor=0.75")
    driver = Chrome(options=chrome_options)
    yield driver


def test_result_contents(browser):
    browser.get('https://demoqa.com/automation-practice-form')
    browser.find_element(By.ID, "firstName").send_keys("Hanna")
    browser.find_element(By.ID, "lastName").send_keys("Rudzenka")
    browser.find_element(By.ID, "userEmail").send_keys("HannaRudzenka@gmail.com")
    browser.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']").click()
    browser.find_element(By.CSS_SELECTOR, "input#userNumber").send_keys('5555544444')
    browser.find_element(By.ID, "subjectsInput").send_keys('Maths')
    browser.find_element(By.ID, "react-select-2-option-0").click()
    browser.find_element(By.ID, "currentAddress").send_keys('Wroclaw, Skwierynska 20A')
    browser.find_element(By.ID, "dateOfBirthInput").click()
    Select(browser.find_element(By.CLASS_NAME, "react-datepicker__month-select")).select_by_visible_text('August')
    browser.find_element(By.CLASS_NAME, "react-datepicker__day--013").click()
    browser.find_element(By.ID, "state").click()
    browser.find_element(By.ID, "react-select-3-option-0").click()
    browser.find_element(By.ID, "city").click()
    browser.find_element(By.ID, "react-select-4-option-2").click()
    browser.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']").click()
    browser.find_element(By.ID, "submit").click()
    browser.find_element(By.CLASS_NAME, "modal-content").is_displayed()
    item_contents = [i.text for i in browser.find_elements(By.CSS_SELECTOR, "tbody>tr")]
    print(item_contents)
