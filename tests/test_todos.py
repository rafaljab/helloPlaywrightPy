from playwright.sync_api import expect


def test_add_todos(todos_page):
    # Given
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
