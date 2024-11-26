from playwright.sync_api import Page, BrowserContext, expect


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_button = page.get_by_role('link', name='Click')
    with context.expect_page() as new_page:
        click_button.click()
    new_page = new_page.value
    result_text = new_page.locator('#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')
    expect(click_button).to_be_enabled()
