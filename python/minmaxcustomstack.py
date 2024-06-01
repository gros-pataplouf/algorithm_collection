class Stack:
    # Any of the initial methods can be updated
    def __init__(self):
        self.stack = []
        self.max_lst = []
        self.min_lst = []

    def peek(self):
        return self.stack[-1]

    def push(self, item):
        if not self.max_lst or self.max_lst[-1] <= item:
            self.max_lst.append(item)
        if not self.min_lst or self.min_lst[-1] >= item:
            self.min_lst.append(item)
        self.stack.append(item)
        return item

    def pop(self):
        if self.max_lst[-1] == self.stack[-1]:
            self.max_lst.pop()
        if self.min_lst[-1] == self.stack[-1]:
            self.min_lst.pop()
        return self.stack.pop()


    def get_stack_max(self):
        return self.max_lst[-1]


    def get_stack_min(self):
        return self.min_lst[-1]

newstack = Stack()
for item in [3, 5, 6, 8, 2, 4, 9, 1]:
    newstack.push(item)
newstack.pop()
print(newstack.get_stack_max())
print(newstack.get_stack_min())