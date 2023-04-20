from time import sleep
from todomvc_testing.Model import todos

def test_add():
    todos.given_opened('11', '22', '33', '44')
    assert todos.should_be('11', '22', '33', '44')
def test_mark():
    todos.toggle('22')
    assert todos.should_be_completed('22')
def test_clear_complete():
    todos.clear_completed()
    assert todos.should_be_active('11', '33', '44')
def test_edit():
    todos.edit('33', '3+')
    assert todos.should_be_active('11', '3+', '44')
def test_deleted():
    todos.delete('3+')
    assert todos.should_be_active('11', '44')
    sleep(5)
