from selene import have, command
from selene.support.shared import browser

completed = have.css_class('completed')


class TodoMVC:
    def __init__(self):
        self.todo_list = browser.all('#todo-list>li')

    def open(self):
        browser.open('http://todomvc.com/examples/emberjs')
        return self

    def add(self, *todos: str):
        for todo in todos:
            browser.element('#new-todo').type(todo).press_enter()
        return self

    def given_opened(self, *todos: str):
        self.open()
        self.add(*todos)

    def should_be(self, *todos: str):
        self.todo_list.should(have.exact_texts(*todos))
        return self

    def start_editing(self, todo, new_text):
        self.todo_list.element_by(have.exact_text(todo)).double_click()
        return self.todo_list.element_by(have.css_class('editing')).element('.edit').perform(
            command.js.set_value(new_text))

    def edit(self, todo, new_text):
        self.start_editing(todo, new_text).press_enter()
        return self

    def edit_by_focus_change(self, todo, new_text):
        self.start_editing(todo, new_text).press_tab()
        return self

    def cancel_edit(self, *todos: str, new_text):
        self.start_editing(*todos, new_text).press_escape()

    def toggle(self, *todos: str):
        self.todo_list.element_by(have.exact_text(*todos)).element('.toggle').click()
        return self

    def toggle_all(self):
        browser.element('#toggle-all').click()
        return self

    def should_be_completed(self, *todos: str):
        self.todo_list.filtered_by(completed).should(have.exact_texts(*todos))
        return self

    def should_be_active(self, *todos: str):
        self.todo_list.filtered_by(completed.not_).should(have.exact_texts(*todos))
        return self

    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

    def delete(self, *todos: str):
        self.todo_list.element_by(have.exact_text(*todos)).hover().element('.destroy').click()
        return self
