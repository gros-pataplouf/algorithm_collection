"""https://skilled.dev/course/implement-a-linked-list
The most common way to be asked a linked list interview question is to be given the head node of a singly linked list. Since you are only given the head, you know that you don't have access to a wrapper class or the tail node, so all operations must happen by iterating from the beginning.
When you are given this node as an input, it will already be instantiated and have a value for its data and next.
Instead of creating a special linked list object, we will write functions that take a head node and performs a prepend, append, insert, and delete operation in the same manner as how you will use them in an interview. See the final implementation in a REPL.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self
        return new_head
    def append(self, data):
        next = self.next
        if self.next is None:
            self.next = Node(data)
            return self.next
        return next.append(data)
    def insert(self, data, node_before):
        inserted_node = Node(data)
        inserted_node.next = node_before.next
        node_before.next = inserted_node        
    def delete(self, index):
        current = self
        previous = None
        counter = 0
        while counter < index:
            if current.next is None:
                raise IndexError(f"Index {index} out of range in linked list with tail at index {counter}")
            previous = current
            current = current.next
            counter += 1
        if counter == index:
            if previous:
                previous.next = current.next
            valOfcurrent = (current, current.data)
            del(current)
            return valOfcurrent


node1 = Node("i am the initial head")
node0 = node1.prepend("i am the new head")
node0.append("i am the new tail")
node0.append("i am yet a newer tail")
print(node1.delete(0))