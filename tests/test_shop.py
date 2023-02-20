import pytest

from playwright.sync_api import expect


def test_open_empty_cart(shop_page):
    # Given
    expect(shop_page.empty_cart_text).not_to_be_visible()

    # When
    shop_page.view_cart()

    # Then
    expect(shop_page.empty_cart_text).to_be_visible()


@pytest.mark.parametrize(
    'product_name, total_items, total_price',
    [
        ('Watch', 1, '$99.99'),
        ('iPhone 6', 1, '$499.99'),
        ('MacBook', 1, '$999.99')
    ]
)
def test_add_product_to_cart(shop_page, product_name, total_items, total_price):
    # Given
    expect(shop_page.product_card_button(product_name)).to_have_attribute('title', 'Add Product')
    expect(shop_page.shop_header_total_items).to_have_text('Total Items: 0')
    expect(shop_page.shop_header_total_price).to_have_text('Total Price: $0.00')

    # When
    shop_page.add_product_to_cart(product_name)

    # Then
    expect(shop_page.product_card_button(product_name)).to_have_attribute('title', 'Product In Cart')
    expect(shop_page.shop_header_total_items).to_have_text(f'Total Items: {total_items}')
    expect(shop_page.shop_header_total_price).to_have_text(f'Total Price: {total_price}')
