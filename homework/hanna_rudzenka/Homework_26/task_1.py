from playwright.sync_api import Page


def test_fill_in_registration_form(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('tomsmith')
    page.get_by_role('textbox', name='password').fill('SuperSecretPassword!')
    page.get_by_role('button', name=' Login').click()
