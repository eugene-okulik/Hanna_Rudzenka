from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_2():
    driver = Chrome()
    driver.implicitly_wait(3)
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    ActionChains(driver).scroll_by_amount(0, 700).perform()
    first_elem = driver.find_element(By.CLASS_NAME, 'product-image-photo')
    ActionChains(driver).move_to_element(first_elem).perform()
    add_to_compare_btn = driver.find_element(By.CLASS_NAME, 'tocompare')
    ActionChains(driver).click(add_to_compare_btn).perform()
    ActionChains(driver).scroll_by_amount(0, 1000).perform()
    compare_products_item_text = driver.find_element(By.XPATH, "//*[@id='compare-items']/li/strong/a").text
    assert compare_products_item_text == "Push It Messenger Bag"
