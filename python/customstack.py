"""
stack implementation
is like linked list, no access to tail needed bc FILO
implement node (node only needs to know its next, not previous)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    def push(self, node):
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        return self.top
    def pop(self):
        popped_element = self.top
        self.top = self.top.next if self.top.next else None
        return popped_element
    def peek(self):
        return self.top
    

