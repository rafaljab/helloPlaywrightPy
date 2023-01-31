import pytest

from pom.left_menu import LeftMenuFragment
from pom.login import LoginPage


@pytest.fixture
def login_page(page):
    login_page = LoginPage(page)
    login_page.navigate()
    yield login_page


@pytest.fixture
def login(login_page):
    login_page.login(email='admin@example.com', password='admin123')
    yield


@pytest.fixture
def left_menu(page, login):
    left_menu = LeftMenuFragment(page)
    yield left_menu


@pytest.fixture
def shop_page(left_menu):
    shop_page = left_menu.click_shop()
    yield shop_page
