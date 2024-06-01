import itertools
from math import pi


#count

counter = itertools.count(start=12, step=-pi)

my_data = [200, 500, 230, 400, 700]

# print(list(enumerate(my_data)))

# print(list(zip(counter, my_data)))

print(list(zip(itertools.zip_longest(range(100)), my_data)))


print(next(counter))

#cycle
cycler = itertools.cycle([1, 2, 4, 7, 2])  #also works with tuples

repeater = itertools.repeat(2, times=4) #repeats until hits stopiteration
print(next(repeater))
print(next(repeater))
print(next(repeater))

#reuse the same value in a map function
squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))

#starmap
squares2 = itertools.starmap(pow, [(0,2), (1,2), (2,2), (2,3)])

print(list(squares2))
print(next(cycler))
print(next(cycler))

#combinations and permutations

letters = ['a', 'b', 'c', 'd']

result = itertools.combinations(letters, 2) # all combinations of 2 values
for item in result:
    print(item)

result = itertools.permutations(letters, 2) # all combinations of 2 values
for item in result:
    print(item)

numbers = [1, 2, 4, 3]
result = itertools.product(numbers, repeat=4)
for item in result:
    print(item)

items = ['apples', 'eggs', 'oranges', 'bread', 'milk']

chained = itertools.chain(letters, numbers, items) #eats up less 

for element in chained:
    print(element)

#islice allows slicing on an iterator from a to b
# one arg =  iterable
# two args = start
# three args = stopping point
 # four args = step
 #3rd arg: stp
 # usecase: grab slice of logfile
sliced = itertools.islice(range(20), 5, 10, 2)
for elt in sliced:
    print(elt)
with open('test.log', 'r') as f:
    header = itertools.islice(f, 3)
    for line in header:
        print(line, end='')

#the compress function
selectors = [True, False, True, True, False, False, True, False]

result = itertools.compress(letters, selectors)
for item in result:
    print(result)
    