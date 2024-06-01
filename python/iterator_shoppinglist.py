class ShoppingList:
    def __init__(self):
        self.lst = []
        self.n = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < len(self.lst):
            item = self.lst[self.n]
            self.n += 1
            return item
        else:
            raise StopIteration
    def add(self, item, quantity):
        self.lst.append((item, quantity))


shopping_list = ShoppingList()
shopping_list.add("bananas", 10)
shopping_list.add("apples", 5)
shopping_list.add("pineapple", 1)

for product in shopping_list:
    print(f"{product[0]}: {product[1]} units")