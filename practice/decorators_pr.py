from functools import wraps
# Functions in Python - objects!.


def test_decorator(func):
    # will preserve information about the original function
    # For example:
    # without this annotation some_func.__name__ will return 'wrapper'
    # with this annotation some_func.__name__ will return 'some_func'

    @wraps(func)
    def wrapper(first, second):
        print('some text in decorator')
        result = func(first, second)
        return result

    return wrapper


@test_decorator
def some_func(first, second):
    print('text in func')
    return first + second


def start_with_k(func):
    def wrapper(*args):
        func(*args)
        if args[0].startswith('K'):
            print('Text starts with "K".')
    return wrapper


@start_with_k
def print_text(text):
    print(text)


def typped(type_):
    def real_decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f"Should be {type_}")
            return func(*args)
        return wrapper
    return real_decorator


@typped(int)
def calculate(a, b, c):
    return a + b + c


if __name__ == '__main__':
    # print(calculate(5, 4, 2))
    b = 8
    print(f"{b=}")
