import pytest

from playwright.sync_api import expect


def test_open_empty_cart(shop_page):
    # Given
    expect(shop_page.empty_cart_text).not_to_be_visible()

    # When
    shop_page.view_cart()

    # Then
    expect(shop_page.empty_cart_text).to_be_visible()
    expect(shop_page.place_order_button).to_be_disabled()


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


def test_add_multiple_products_to_cart(shop_page):
    # Given
    expect(shop_page.shop_header_total_items).to_have_text('Total Items: 0')
    expect(shop_page.shop_header_total_price).to_have_text('Total Price: $0.00')

    # When
    shop_page.add_product_to_cart('Watch')
    shop_page.add_product_to_cart('iPhone 6')
    shop_page.add_product_to_cart('MacBook')
    shop_page.add_product_to_cart('Watch')

    # Then
    expect(shop_page.shop_header_total_items).to_have_text('Total Items: 4')
    expect(shop_page.shop_header_total_price).to_have_text('Total Price: $1,699.96')


def test_change_number_of_product_items_in_cart(shop_page):
    # Given
    product_name = 'Watch'

    shop_page.add_product_to_cart(product_name)
    shop_page.view_cart()

    expect(shop_page.shop_header_total_items).to_have_text('Total Items: 1')
    expect(shop_page.shop_header_total_price).to_have_text('Total Price: $99.99')
    expect(shop_page.product_cart_item_badge(product_name)).to_have_text('1')
    expect(shop_page.product_cart_item_quantity_dropdown(product_name)).to_have_text('1')
    expect(shop_page.product_cart_item_subtotal_price(product_name)).to_have_text('Subtotal Price: $99.99')

    # When
    shop_page.change_quantity_of_product(product_name, 10)

    # Then
    expect(shop_page.shop_header_total_items).to_have_text('Total Items: 10')
    expect(shop_page.shop_header_total_price).to_have_text('Total Price: $999.90')
    expect(shop_page.product_cart_item_badge(product_name)).to_have_text('10')
    expect(shop_page.product_cart_item_quantity_dropdown(product_name)).to_have_text('10')
    expect(shop_page.product_cart_item_subtotal_price(product_name)).to_have_text('Subtotal Price: $999.90')


def test_remove_product_item_from_cart(shop_page):
    # Given
    product_name = 'Watch'

    shop_page.add_product_to_cart(product_name)
    shop_page.view_cart()

    expect(shop_page.product_cart_item(product_name)).to_be_visible()
    expect(shop_page.empty_cart_text).not_to_be_visible()
    expect(shop_page.place_order_button).to_be_enabled()

    # When
    shop_page.remove_product_from_cart(product_name)

    # Then
    expect(shop_page.product_cart_item(product_name)).not_to_be_visible()
    expect(shop_page.empty_cart_text).to_be_visible()
    expect(shop_page.place_order_button).to_be_disabled()


def test_end_to_end_place_order(shop_page):
    # Given
    products_to_order = [
        {
            'product_name': 'Watch',
            'quantity': 3,  # 0 <= quantity
            'quantity_by_dropdown': False
        },
        {
            'product_name': 'iPhone 6',
            'quantity': 5,
            'quantity_by_dropdown': True
        },
        {
            'product_name': 'MacBook',
            'quantity': 1,
            'quantity_by_dropdown': None
        }
    ]
    total_quantity = 9
    total_price = '$3,799.91'

    # When
    for product in products_to_order:
        shop_page.add_product_to_cart(product['product_name'])

        if product['quantity_by_dropdown'] or product['quantity_by_dropdown'] is None:
            shop_page.view_cart()
            if product['quantity'] > 0:
                shop_page.change_quantity_of_product(product['product_name'], product['quantity'])
            else:
                shop_page.remove_product_from_cart(product['product_name'])
            shop_page.browse_products()
        else:
            for i in range(product['quantity']-1):
                shop_page.add_product_to_cart(product['product_name'])

    shop_page.view_cart()

    expect(shop_page.shop_header_total_items).to_have_text(f'Total Items: {total_quantity}')
    expect(shop_page.shop_header_total_price).to_have_text(f'Total Price: {total_price}')

    shop_page.place_order()

    # Then
    expect(shop_page.shop_header_total_items).to_have_text('Total Items: 0')
    expect(shop_page.shop_header_total_price).to_have_text('Total Price: $0.00')
    expect(shop_page.after_order_text).to_be_visible()
