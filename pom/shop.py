from playwright.sync_api import Page, Locator

from config import BASE_URL


class ShopPage:
    url = f'{BASE_URL}shop'

    def __init__(self, page: Page):
        self.page = page

        self.view_cart_button: Locator = page.get_by_role('button', name='View Cart')
        self.browse_products_button: Locator = page.get_by_role('button', name='Browse Products')
        self.empty_cart_text: Locator = page.get_by_text('There\'s nothing in your cart!')
        self.product_cards: Locator = page.get_by_test_id('product-card')
        self.shop_header_total_items = page.get_by_test_id('shop-header-total-items')
        self.shop_header_total_price = page.get_by_test_id('shop-header-total-price')

    def navigate(self):
        self.page.goto(self.url)

    def view_cart(self):
        self.view_cart_button.click()

    def browse_products(self):
        self.browse_products_button.click()

    def add_product_to_cart(self, product_name: str):
        self.product_cards.filter(has_text=product_name).get_by_role('button').click()
