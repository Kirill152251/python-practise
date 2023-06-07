from functools import wraps


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


print(some_func(1, 2))
print(some_func.__name__)
