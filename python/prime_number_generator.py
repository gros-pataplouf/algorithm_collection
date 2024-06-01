from time import perf_counter
def get_prime_numbers_memo_list(counter=1, end=None):

    counter = counter
    prime_numbers = []
    #def prime num: can only be divided by itself and one
    while True:
        counter += 1
        smaller_nums = [x for x in range(2, round(counter**0.5)+1)]
        divided = [y for y in smaller_nums if counter%y == 0 if y in prime_numbers]
        if not divided:
            prime_numbers.append(counter)
            yield counter

def get_prime_numbers_no_memo(counter=1, end=None):

    counter = counter
    #def prime num: can only be divided by itself and one
    while True:
        counter += 1
        divided = [x for x in range(2, round(counter**0.5)+1) if counter%x == 0]
        #divided = [y for y in smaller_nums if counter%y == 0]
        if not divided:
            yield counter

def get_prime_numbers_memo_set(counter=1, end=None):

    counter = counter
    prime_numbers = set()
    #def prime num: can only be divided by itself and one
    while True:
        counter += 1
        smaller_nums = [x for x in range(2, round(counter**0.5)+1)]
        divided = [y for y in smaller_nums if counter%y == 0 if y in prime_numbers]
        if not divided:
            prime_numbers.add(counter)
            yield counter

def get_prime_numbers_memo_dict(counter=1, end=None):
    counter = counter
    prime_numbers = {}
    #def prime num: can only be divided by itself and one
    while True:
        counter += 1
        smaller_nums = [x for x in range(2, round(counter**0.5)+1)]
        divided = [y for y in smaller_nums if counter%y == 0 if y in prime_numbers]
        if not divided:
            prime_numbers[counter] = counter
            yield counter



prime_numbers = get_prime_numbers_memo_list()
prime_numbers2 = get_prime_numbers_no_memo()
prime_numbers3 = get_prime_numbers_memo_set()
prime_numbers4 = get_prime_numbers_memo_dict()

upper = 50000
# t1 = perf_counter()
# for i in range(1,upper):
#     next(prime_numbers)
# t2 = perf_counter()
# print("with memo list it took", upper, t2-t1)

t3 = perf_counter()
for i in range(1,upper):
    next(prime_numbers2)
t4 = perf_counter()
print("without memoization it took", upper, t4-t3)

t5 = perf_counter()
for i in range(1,upper):
    next(prime_numbers3)
t6 = perf_counter()
print("with a set it took", upper, t6-t5)

t7 = perf_counter()
for i in range(1,upper):
    next(prime_numbers4)
t8 = perf_counter()
print("with a dict it took", upper, t8-t7)
