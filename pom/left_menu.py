from playwright.sync_api import Page, Locator

from pom.shop import ShopPage


class LeftMenuFragment:
    def __init__(self, page: Page):
        self.page = page

        self.home_link: Locator = page.get_by_role('link', name='Home')
        self.shop_link: Locator = page.get_by_role('link', name='Shop')

    def click_home(self):
        self.home_link.click()

    def click_shop(self):
        self.shop_link.click()
        return ShopPage(self.page)
