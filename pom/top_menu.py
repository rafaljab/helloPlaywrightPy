from playwright.sync_api import Page, Locator


class TopMenuFragment:
    def __init__(self, page: Page):
        self.page = page

        self.hamburger_button: Locator = page.get_by_test_id('MenuIcon')

    def open_menu(self):
        self.hamburger_button.click()
