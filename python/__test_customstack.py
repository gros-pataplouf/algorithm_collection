import pytest
from customstack import Node, Stack

def test_node_contains_given_data():
    mynode = Node("testdata")
    assert mynode.data == "testdata" and mynode.next is None

def test_stack_empty():
    mystack = Stack()
    assert mystack.top is None

def test_push_single_elt_to_empty():
    node = Node("my beautiful node")
    stack = Stack()
    stack.push(node)
    assert stack.top == node

def test_push_more_nodes():
    nodes = list(map(lambda elt: Node(elt), [23, True, "blue lemon", "schmetterling"]))
    stack = Stack()
    for node in nodes:
        stack.push(node)
    assert stack.top.data == nodes[-1].data and stack.top.next.data == nodes[-2].data


def test_pop_node():
    nodes = list(map(lambda elt: Node(elt), [23, True, "blue lemon", "schmetterling"]))
    stack = Stack()
    for node in nodes:
        stack.push(node)
    assert stack.pop().data == "schmetterling" and stack.top == nodes[-2]

def test_peek():
    nodes = list(map(lambda elt: Node(elt), [23, True, "blue lemon", "schmetterling"]))
    stack = Stack()
    for node in nodes:
        stack.push(node)
    assert stack.peek() == nodes[-1]


