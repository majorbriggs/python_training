from functools import wraps

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return "<{tag_name}>{result}</{tag_name}>".format(tag_name=tag_name, result=result)
        return wrapper
    return tags_decorator

@tags('div')
@tags('p')
@tags('span')
@tags('strong')
def greet(name):
    return "Hello " + name


print(greet("My Friend"))


def outer_decorator(some_parameter):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            print("Decorator got the parameter: {}".format(some_parameter))
            print("Decorated function starts")
            result = func(*args, **kwargs)
            print("Decorated function finished.")
            return result

            # inner function uses the parameter from the outer-most function

        return wrapper

    return real_decorator


@outer_decorator("Some parameter")
def test_step():
    print("Do something")



test_step()
