class DynamicArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    def get(self, index):
        return self.data[index]
    def push(self, value):
        self.data[len(self.data)] = value
    def pop(self):
        removed_element = self.data[len(self.data) - 1]
        del self.data[len(self.data) - 1]
        return removed_element
    def insert(self, element, index):
        self.data[len(self.data)] = None
        i = len(self.data) - 1
        while i > index:
            self.data[i] = self.data[i-1]
            i -= 1
            # if key >= index:
            #     self.data[key+1] = value
        self.data[index] = element

my_array = DynamicArray()
my_array.push("dog")
my_array.push("cat")
my_array.push("squirrel")
my_array.insert("goldfish", 1)
print(my_array.data)

#Correction
class DynamicArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

        return self.length

    def pop(self):
        if self.length == 0:
            return None

        popped_item = self.data[self.length - 1]
        self.data[self.length - 1] = None
        self.length -= 1

        return popped_item

    def insert(self, index, item):
        if index > self.length - 1 or index < 0:
            return None

        self.length += 1

        for i in range(self.length - 1, index - 1, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = item

        return self.data

    def remove(self, index):
        if self.length == 0:
            return None

        if index > self.length - 1 or index < 0:
            return None

        item_to_be_removed = self.data[index]

        for i in range(index, self.length - 1):
            self.data[i] = self.data[i+1]

        self.data[self.length - 1] = None
        self.length -= 1

        return item_to_be_removed