from playwright.sync_api import Page, Locator

from config import BASE_URL


class TodosPage:
    url = f'{BASE_URL}todos'

    def __init__(self, page: Page):
        self.page = page

        self.new_task_input_field: Locator = page.get_by_role('textbox')
        self.add_task_button: Locator = page.get_by_role('button', name='ADD TASK')
        self.clear_tasks_button: Locator = page.get_by_role('button', name='CLEAR COMPLETED TASKS')
        self.todo_items: Locator = page.locator('div.MuiFormGroup-root.css-dmmspl-MuiFormGroup-root > label')

    def navigate(self):
        self.page.goto(self.url)

    def add_task(self, task_name: str):
        self.new_task_input_field.type(task_name)
        self.add_task_button.click()
