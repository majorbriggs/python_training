def log(func):
    def wrapper(*args, **kwargs):
        print("{} start".format(func.__name__))
        func(*args, **kwargs)
        print("{} stop".format(func.__name__))
    return wrapper

@log
def print_something():
    print("Test")


print_something()



def tags(tag_name):
    def tags_decorator(func):
        def wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return wrapper
    return tags_decorator

@tags('div')
@tags('p')
@tags('strong')
def greet(name):
    return "Hello " + name


print(greet("My Friend"))