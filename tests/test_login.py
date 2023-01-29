import pytest
from playwright.sync_api import expect

from config import BASE_URL

from pom.login import LoginPage


@pytest.fixture
def login_page(page):
    login_page = LoginPage(page)
    login_page.navigate()
    yield login_page


def test_login_with_correct_data(login_page):
    # Given
    email = 'admin@example.com'
    password = 'admin123'

    # When
    login_page.login(email=email, password=password)

    # Then
    expect(login_page.page).to_have_url(BASE_URL)
    expect(login_page.alert_notification).to_be_hidden()


def test_login_with_incorrect_email(login_page):
    # Given
    email = 'test@example.com'
    password = 'admin123'

    # When
    login_page.login(email=email, password=password)

    # Then
    expect(login_page.page).to_have_url(login_page.url)
    expect(login_page.alert_notification).to_be_visible()


def test_login_with_incorrect_password(login_page):
    # Given
    email = 'admin@example.com'
    password = 'test'

    # When
    login_page.login(email=email, password=password)

    # Then
    expect(login_page.page).to_have_url(login_page.url)
    expect(login_page.alert_notification).to_be_visible()
