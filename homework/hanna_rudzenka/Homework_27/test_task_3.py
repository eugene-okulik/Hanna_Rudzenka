import time

from playwright.sync_api import Page, expect


def test_fill_and_accept(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_change_locator = page.locator('#colorChange')
    expect(color_change_locator).to_have_css('color', 'rgb(220, 53, 69)')
    color_change_locator.click()
