from functools import wraps


def verbose(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("{} function starts".format(func.__name__))
        result = func(*args, **kwargs)
        print("{} function finished".format(func.__name__))
        return result
    return wrapper

@verbose
def print_something():
    print("Test")


print_something()





from functools import wraps


def verbose(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("{} function starts".format(func.__name__))
        func(*args, **kwargs)
        print("{} function finished".format(func.__name__))

    return wrapper


@verbose
def test_step_1():
    print("Do something")