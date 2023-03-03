from playwright.sync_api import Page, Locator

from config import BASE_URL


class TodosPage:
    url = f'{BASE_URL}/todos'

    def __init__(self, page: Page):
        self.page = page

        self.new_task_input_field: Locator = page.get_by_role('textbox')
        self.add_task_button: Locator = page.get_by_role('button', name='ADD TASK')
        self.clear_tasks_button: Locator = page.get_by_role('button', name='CLEAR COMPLETED TASKS')
        self.todo_items: Locator = page.get_by_test_id('todo-item')
        self.no_todos_paragraph: Locator = page.get_by_role('paragraph').filter(has_text='There are no TODOs!')

    def navigate(self):
        self.page.goto(self.url)

    def add_task(self, task_name: str):
        self.new_task_input_field.type(task_name)
        self.add_task_button.click()

    def todo_item(self, todo_name: str) -> Locator:
        return self.todo_items.filter(has_text=todo_name)

    def todo_item_checkbox(self, todo_name: str) -> Locator:
        return self.todo_item(todo_name).get_by_role('checkbox')

    def toggle_todo_item(self, todo_name: str):
        todo_item_checkbox = self.todo_item_checkbox(todo_name)
        if todo_item_checkbox.is_checked():
            todo_item_checkbox.uncheck()
        else:
            todo_item_checkbox.check()

    def clear_completed_tasks(self):
        self.clear_tasks_button.click()
