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
        pass

    def dequeue(self):
        # remove the first item from the list
        pass