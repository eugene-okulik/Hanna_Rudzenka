from playwright.sync_api import Page


def test_fill_in_registration_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Hanna')
    page.get_by_placeholder('Last Name').fill('Rudzenka')
    page.get_by_placeholder('name@example.com').fill('ann@mail.ru')
    page.locator('label.custom-control-label[for="gender-radio-2"]').click()
    page.get_by_placeholder('Mobile Number').fill('12345678910')
    page.locator('input#dateOfBirthInput').click()
    page.locator('.react-datepicker__day--026').click()
    page.locator('#subjectsInput').fill('Ma')
    page.locator('#react-select-2-option-0').click()
    page.locator('label.custom-control-label[for="hobbies-checkbox-1"]').click()
    page.get_by_placeholder('Current Address').fill('Wroclaw, Skwierzynska 20A/9')
    page.locator('#state').click()
    page.locator('#react-select-3-option-0').click()
    page.locator('#city').click()
    page.locator('#react-select-4-option-2').click()
    page.get_by_role('button', name='Submit').click()
