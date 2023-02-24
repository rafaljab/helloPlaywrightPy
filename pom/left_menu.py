from playwright.sync_api import Page, Locator

from pom.shop import ShopPage
from pom.todos import TodosPage


class LeftMenuFragment:
    def __init__(self, page: Page):
        self.page = page

        self.home_link: Locator = page.get_by_role('link', name='Home')
        self.shop_link: Locator = page.get_by_role('link', name='Shop')
        self.todos_link: Locator = page.get_by_role('link', name='TODOs')

    def click_home(self):
        self.home_link.click()

    def click_shop(self):
        self.shop_link.click()
        return ShopPage(self.page)

    def click_todos(self):
        self.todos_link.click()
        return TodosPage(self.page)
