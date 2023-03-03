import json

import pytest

from config import DOMAIN

from pom.left_menu import LeftMenuFragment
from pom.login import LoginPage
from pom.todos import TodosPage


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


@pytest.fixture
def todos_page(left_menu):
    todos_page = left_menu.click_todos()
    yield todos_page


@pytest.fixture(scope='session')
def todos_page_with_state(browser):

    with open('tests/test_data/todos_state.json') as f:
        data = json.load(f)

    data['origins'][0]['origin'] = data['origins'][0]['origin'].replace('$domain', f'{DOMAIN}/')

    context = browser.new_context(storage_state=data)
    page = context.new_page()
    todos_page = TodosPage(page)
    todos_page.navigate()

    yield todos_page

    context.close()
    browser.close()
