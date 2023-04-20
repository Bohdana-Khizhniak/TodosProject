# from time import sleep
#
# from selene import have, command
# from selene.support.shared import browser
#
# browser.config.hold_browser_open = True
# browser.open('http://todomvc.com/examples/emberjs')
#
# browser.element('#new-todo').type('a').press_enter()
# browser.element('#new-todo').type('b').press_enter()
#
# browser.all('#todo-list>li').should(have.exact_texts('a', 'b'))
# browser.all('#todo-list>li').element_by(have.exact_text('b')).double_click()
# browser.all('#todo-list>li').element_by(have.css_class('editing')).element('.edit')\
#     .perform(command.js.set_value('b+')).press_enter()
# browser.all('#todo-list>li').element_by(have.exact_text('b+')).element('.toggle').click()
# browser.element('#clear-completed').click()
# browser.all('#todo-list>li').should(have.exact_texts('a'))
# browser.all('#todo-list>li').element_by(have.exact_text('a')).double_click()
# browser.all('#todo-list>li').element_by(have.css_class('editing')).element('.edit')\
#     .perform(command.js.set_value('to be canceled')).press_escape()
# browser.all('#todo-list>li').element_by(have.exact_text('a')).hover().element('.destroy').click()
# browser.all('#todo-list>li').should(have.size(0))
#
# sleep(40)
