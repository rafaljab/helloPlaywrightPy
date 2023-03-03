from playwright.sync_api import expect


def test_add_todos(todos_page_authenticated):
    # Given
    todos_page = todos_page_authenticated

    tasks = [
        'Buy milk',
        'Go for a walk',
        'Wash the dishes'
    ]
    expect(todos_page.todo_items).not_to_be_visible()

    # When
    for task in tasks:
        todos_page.add_task(task)

    # Then
    assert todos_page.todo_items.count() == len(tasks)
    for todo_text in todos_page.todo_items.all_text_contents():
        assert todo_text in tasks


def test_check_todos_from_state(todos_page_with_state):
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
