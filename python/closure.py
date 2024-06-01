def outer_func():
    message = "Ciao"
    def inner_func():
        print(message)
    return inner_func()

print(outer_func())