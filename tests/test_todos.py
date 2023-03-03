import pytest
from playwright.sync_api import expect


def test_add_todos(todos_page_authenticated):
    # Given
    todos_page = todos_page_authenticated

    tasks = [
        'Buy milk',
        'Go for a walk',
        'Wash the dishes'
    ]
    expect(todos_page.no_todos_paragraph).to_be_visible()
    expect(todos_page.todo_items).not_to_be_visible()

    # When
    for task in tasks:
        todos_page.add_task(task)

    # Then
    assert todos_page.todo_items.count() == len(tasks)
    for todo_text in todos_page.todo_items.all_text_contents():
        assert todo_text in tasks


def test_load_todos_from_state(todos_page_with_state):
    # Given
    todos_page = todos_page_with_state

    tasks = [
        'Buy milk',
        'Go for a walk',
        'Wash the dishes'
    ]
    expect(todos_page.todo_items.first).to_be_visible()

    # When

    # Then
    assert todos_page.todo_items.count() == 3
    for todo_text in todos_page.todo_items.all_text_contents():
        assert todo_text in tasks


def test_toggle_todos(todos_page_with_state):
    # Given
    todos_page = todos_page_with_state

    tasks = [
        'Buy milk',
        'Go for a walk',
        'Wash the dishes'
    ]
    expect(todos_page.todo_item_checkbox(tasks[0])).not_to_be_checked()

    # When
    todos_page.toggle_todo_item(tasks[0])

    # Then
    expect(todos_page.todo_item_checkbox(tasks[0])).to_be_checked()

    # When
    todos_page.toggle_todo_item(tasks[0])

    # Then
    expect(todos_page.todo_item_checkbox(tasks[0])).not_to_be_checked()


def test_clear_todos(todos_page_with_state):
    # Given
    todos_page = todos_page_with_state

    tasks = [
        'Buy milk',
        'Go for a walk',
        'Wash the dishes'
    ]
    expect(todos_page.todo_item(tasks[0])).to_be_visible()
    expect(todos_page.todo_item(tasks[1])).to_be_visible()
    expect(todos_page.todo_item(tasks[2])).to_be_visible()

    # When
    todos_page.toggle_todo_item(tasks[0])
    todos_page.clear_completed_tasks()

    # Then
    expect(todos_page.todo_item(tasks[0])).not_to_be_visible()
    expect(todos_page.todo_item(tasks[1])).to_be_visible()
    expect(todos_page.todo_item(tasks[2])).to_be_visible()

    # When
    todos_page.toggle_todo_item(tasks[1])
    todos_page.clear_completed_tasks()

    # Then
    expect(todos_page.todo_item(tasks[0])).not_to_be_visible()
    expect(todos_page.todo_item(tasks[1])).not_to_be_visible()
    expect(todos_page.todo_item(tasks[2])).to_be_visible()


@pytest.mark.e2e
def test_todos(todos_page):
    # Given
    tasks = [
        'Buy milk',
        'Go for a walk',
        'Wash the dishes'
    ]
    expect(todos_page.no_todos_paragraph).to_be_visible()

    # When
    todos_page.add_task(tasks[0])
    todos_page.add_task(tasks[1])

    # Then
    expect(todos_page.todo_item(tasks[0])).to_be_visible()
    expect(todos_page.todo_item(tasks[1])).to_be_visible()
    expect(todos_page.no_todos_paragraph).not_to_be_visible()

    # When
    todos_page.toggle_todo_item(tasks[1])
    todos_page.clear_completed_tasks()

    # Then
    expect(todos_page.todo_item(tasks[0])).to_be_visible()
    expect(todos_page.todo_item(tasks[1])).not_to_be_visible()
    expect(todos_page.no_todos_paragraph).not_to_be_visible()

    # When
    todos_page.add_task(tasks[2])

    # Then
    expect(todos_page.todo_item(tasks[0])).to_be_visible()
    expect(todos_page.todo_item(tasks[1])).not_to_be_visible()
    expect(todos_page.todo_item(tasks[2])).to_be_visible()
    expect(todos_page.no_todos_paragraph).not_to_be_visible()

    # When
    todos_page.toggle_todo_item(tasks[0])
    todos_page.toggle_todo_item(tasks[2])
    todos_page.clear_completed_tasks()

    # Then
    expect(todos_page.todo_item(tasks[0])).not_to_be_visible()
    expect(todos_page.todo_item(tasks[1])).not_to_be_visible()
    expect(todos_page.todo_item(tasks[2])).not_to_be_visible()
    expect(todos_page.no_todos_paragraph).to_be_visible()
