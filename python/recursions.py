import time
import timeit

def timer(func):
    def func_wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{func.__name__} ran in {t2} seconds.")
        return result
    return func_wrapper

@timer
def fibonacci_iterative(n):
    accumulator = 0
    operator = 1
    for i in range(0, n):
        result = accumulator + operator
        accumulator = operator 
        operator = result
    return accumulator

@timer
def fibonacci_recursive(n):
    # Base case
    if n < 2:
        return n
    # Sum the two previous numbers to get the current 
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def reverse_string_iterative(input):
    output = ""
    for i in range(1, len(input) + 1):
        output += input[-i]
    return output


def reverse_string_recursive(input):
    if len(input) <= 2:
        return input
    return reverse_string_recursive(input[-1]) + reverse_string_recursive(input[:-1])


def gen_permutations_rec(str):
    for i in range(0,len(str)):
        permut.append(str)

    #take the first letter, switch to back
    # dev
    # d-ev
    # de-v
    # de + v
    # ed + v