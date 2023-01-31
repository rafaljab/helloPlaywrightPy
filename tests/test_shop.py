from playwright.sync_api import expect


def test_open_empty_cart(shop_page):
    # Given
    expect(shop_page.empty_cart_text).not_to_be_visible()

    # When
    shop_page.view_cart()

    # Then
    expect(shop_page.empty_cart_text).to_be_visible()
