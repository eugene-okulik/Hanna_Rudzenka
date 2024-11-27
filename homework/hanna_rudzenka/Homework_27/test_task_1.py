from playwright.sync_api import Page, expect


def test_alert_accept(page: Page):
    alert_text = 'Ok'
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.on('dialog', lambda alert: alert.accept(alert_text))
    page.get_by_role('link', name='Click').click()
    result_text = page.locator('#result-text')
    expect(result_text).to_have_text(alert_text)
