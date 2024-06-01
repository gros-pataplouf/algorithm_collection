nums = [ 1, 2, 3]
iterator_nums = nums.__iter__()

print(dir(iterator_nums), iterator_nums)

print(next(iterator_nums))
print(next(iterator_nums))
print(next(iterator_nums))


while True:
    try:
        item = next(iterator_nums)
        print(item)
    except StopIteration:
        break

for num in nums:
    print(num)

print(iter(nums)) #or nums.__iter__() -> is iterable

# an object with an __iter__ method is iterable
# an iterator is an object with a state to store where the iteration left off
# gets next value with __next__ method 


class MyRange:
    def __init__(self, start, end) -> None:
        self.value = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

class Sentence:
    def __init__(self, content) -> None:
        self.n = 0
        self.content = content
        self.content_split = self.content.split()
    def __iter__(self):
        return self
    def __next__(self):
        if self.n >= len(self.content_split):
            raise StopIteration
        else:
            current = self.content_split[self.n]
            self.n += 1
            return current

my_sentence = Sentence("I am a teapot")

for word in my_sentence:
    print(word)

def sentence(content):
    for word in content.split():
        yield word

our_sentence = sentence("I understand generators")

for word in our_sentence:
    print(word)

print(dir(our_sentence))