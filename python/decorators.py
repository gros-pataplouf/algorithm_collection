import time
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(name):
    """greet person by their name"""
    return f"Hello {name}!"

counter = 0

calls = []

max_rate_pro_sec = 10.1

def throttle(func):
    def wrapper(*args, **kwargs):
        global calls
        calls.append(time.time())
        if len(calls) >= 2:
            effective_rate = len(calls) / (calls[-1] - calls[0])
            print(effective_rate)
            if effective_rate > max_rate_pro_sec:
                return None
        return func(*args, **kwargs)
    return wrapper

@throttle
def say_hello(name):
    """greet person by their name"""
    return f"Hello {name}!"


for i in range(0, 20):
    time.sleep(0.11)

    print(say_hello("anonymous"))
