def my_counter():
    counter = 0

    def inner(value):
        nonlocal counter
        counter += value
        print(counter)
        return counter

    return inner


first = my_counter()
second = my_counter()
first(1)
first(10)
second(100)
second(333)
