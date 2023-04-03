from time import sleep

# from selene import have
# from selene.support.shared import browser
from todomvc_testing.Model import todos

todos.open()
# browser.config.hold_browser_open = True
# browser.open('http://todomvc.com/examples/emberjs')
todos.given_opened('11', '22', '33', '44')
todos.should_be('11', '22', '33', '44')

# browser.element('#new-todo').type('a').press_enter()
# browser.element('#new-todo').type('b').press_enter()
# browser.element('#new-todo').type('c').press_enter()

browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
browser.all('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click()
browser.element('#clear-completed').click()
#browser.element('//lable[text()="b"]').element('./preceding-sibling::input').click()
browser.all('#todo-list>li').should(have.exact_texts('a', 'c'))
sleep(40)