import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


def test_1():
    driver = Chrome()
    driver.implicitly_wait(3)
    driver.get('https://www.demoblaze.com/index.html')
    samsung_galaxy_s6 = driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    ActionChains(driver).key_down(Keys.CONTROL).click(samsung_galaxy_s6).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.LINK_TEXT, "Add to cart").click()
    time.sleep(2)
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.LINK_TEXT, "Cart").click()
    item_text = driver.find_element(By.CSS_SELECTOR, "#tbodyid > tr > td:nth-child(2)").text
    assert item_text == "Samsung galaxy s6"
