import pytest

from playwright.sync_api import expect


def test_open_empty_cart(shop_page_authenticated):
    # Given
    shop_page = shop_page_authenticated

    expect(shop_page.empty_cart_text).not_to_be_visible()

    # When
    shop_page.view_cart()

    # Then
    expect(shop_page.empty_cart_text).to_be_visible()
    expect(shop_page.place_order_button).to_be_disabled()


@pytest.mark.with_rest_api
@pytest.mark.parametrize(
    'product_name, total_items, total_price',
    [
        ('iPhone 9', 1, '$549.00'),
        ('iPhone X', 1, '$899.00'),
        ('Samsung Universe 9', 1, '$1,249.00')
    ]
)
def test_add_product_to_cart(shop_page_authenticated, product_name, total_items, total_price):
    # Given
    shop_page = shop_page_authenticated

    expect(shop_page.product_card_button(product_name)).to_have_attribute('title', 'Add Product')
    expect(shop_page.shop_header_total_items).to_have_text('Total Items: 0')
    expect(shop_page.shop_header_total_price).to_have_text('Total Price: $0.00')

    # When
    shop_page.add_product_to_cart(product_name)

    # Then
    expect(shop_page.product_card_button(product_name)).to_have_attribute('title', 'Product In Cart')
    expect(shop_page.shop_header_total_items).to_have_text(f'Total Items: {total_items}')
    expect(shop_page.shop_header_total_price).to_have_text(f'Total Price: {total_price}')


@pytest.mark.with_rest_api
def test_add_multiple_products_to_cart(shop_page_authenticated):
    # Given
    shop_page = shop_page_authenticated

    expect(shop_page.shop_header_total_items).to_have_text('Total Items: 0')
    expect(shop_page.shop_header_total_price).to_have_text('Total Price: $0.00')

    # When
    shop_page.add_product_to_cart('iPhone 9')
    shop_page.add_product_to_cart('iPhone X')
    shop_page.add_product_to_cart('Samsung Universe 9')
    shop_page.add_product_to_cart('iPhone 9')

    # Then
    expect(shop_page.shop_header_total_items).to_have_text('Total Items: 4')
    expect(shop_page.shop_header_total_price).to_have_text('Total Price: $3,246.00')


@pytest.mark.with_rest_api
def test_change_number_of_product_items_in_cart(shop_page_authenticated):
    # Given
    shop_page = shop_page_authenticated

    product_name = 'iPhone 9'

    shop_page.add_product_to_cart(product_name)
    shop_page.view_cart()

    expect(shop_page.shop_header_total_items).to_have_text('Total Items: 1')
    expect(shop_page.shop_header_total_price).to_have_text('Total Price: $549.00')
    expect(shop_page.product_cart_item_badge(product_name)).to_have_text('1')
    expect(shop_page.product_cart_item_quantity_dropdown(product_name)).to_have_text('1')
    expect(shop_page.product_cart_item_subtotal_price(product_name)).to_have_text('Subtotal Price: $549.00')

    # When
    shop_page.change_quantity_of_product(product_name, 10)

    # Then
    expect(shop_page.shop_header_total_items).to_have_text('Total Items: 10')
    expect(shop_page.shop_header_total_price).to_have_text('Total Price: $5,490.00')
    expect(shop_page.product_cart_item_badge(product_name)).to_have_text('10')
    expect(shop_page.product_cart_item_quantity_dropdown(product_name)).to_have_text('10')
    expect(shop_page.product_cart_item_subtotal_price(product_name)).to_have_text('Subtotal Price: $5,490.00')


@pytest.mark.with_rest_api
def test_remove_product_item_from_cart(shop_page_authenticated):
    # Given
    shop_page = shop_page_authenticated

    product_name = 'iPhone 9'

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


@pytest.mark.with_rest_api
@pytest.mark.e2e
def test_place_order(shop_page):
    # Given
    products_to_order = [
        {
            'product_name': 'iPhone 9',
            'quantity': 3,  # 0 <= quantity
            'quantity_by_dropdown': False
        },
        {
            'product_name': 'iPhone X',
            'quantity': 5,
            'quantity_by_dropdown': True
        },
        {
            'product_name': 'Samsung Universe 9',
            'quantity': 1,
            'quantity_by_dropdown': None
        }
    ]
    total_quantity = 9
    total_price = '$7,391.00'

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
