class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class CustomQueue:
    def __init__(self):
        self.first = None
        self.last = None
    def peek(self):
        # get the first item of the list
        return self.first

    def enqueue(self, item):
        # add an item to the end of the list
        new_last_node = Node(item)
        new_last_node.prev = self.last
        is_empty_queue = not self.last and not self.first
        if is_empty_queue:
            self.first = new_last_node
            self.last = new_last_node
        else:
            self.last.prev = new_last_node
            self.last = new_last_node
        return new_last_node



    def dequeue(self):
        # remove the first item from the list
        removed_item = self.first
        if not removed_item:
            return None
        if self.first == self.last:
            self.last = None
        self.first = removed_item.prev
        return removed_item