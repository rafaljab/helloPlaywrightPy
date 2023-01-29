from playwright.sync_api import Page, Locator

from config import BASE_URL


class LoginPage:
    url = f'{BASE_URL}login'

    def __init__(self, page: Page):
        self.page = page

        self.email_field: Locator = page.locator('#email')
        self.pass_field: Locator = page.locator('#password')
        self.login_btn: Locator = page.locator('button[type="submit"]')
        self.alert_notification: Locator = page.locator('div[role="alert"]')

    def navigate(self):
        self.page.goto(self.url)

    def login(self, email, password):
        self.email_field.fill(email)
        self.pass_field.fill(password)
        self.login_btn.click()
