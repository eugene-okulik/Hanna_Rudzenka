import json
import re

from playwright.sync_api import Page, Route


def test_change_response(page: Page):
    iphone_16_pro_new_header = "яблокофон 16 про"

    def response_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = iphone_16_pro_new_header
        body = json.dumps(body)
        route.fulfill(body=body, headers={**response.headers}, response=response)

    page.route(re.compile('/step0_iphone/digitalmat'),
               response_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('.rf-hcard-content-title').first.click()
    page.wait_for_load_state('networkidle')
    pop_up_header_text = ''.join(page.locator("[data-autom='DigitalMat-overlay-header-0-0']").all_inner_texts())
    assert pop_up_header_text == iphone_16_pro_new_header
