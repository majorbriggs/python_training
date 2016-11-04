import time
import requests

def wait_until(condition, timeout=10, raise_exception=True, msg=""):
    """
    Wait until the condition returned by 'condition' function is fulfilled,
    or the timeout is expired. The condition should be checked every 100ms

    Args:
        condition: a function that checks a condition and returns True or False
        timeout: maximal timeout after which the function will raise TimeoutException
                or return False (if raise_exception is False)
        msg: message added to the TimeoutException
    Returns:
        True when the condition is fulfilled within the timeout,
        False when the condition is not fulfilled within the timeout
                and 'raise_exception' is False
    Raises:
        TimeoutException: if raise_exception is True
                        and the condition is not fulfilled within timeout

    """

    t0 = time.time()

    while time.time() - t0 < timeout:
        if condition():
            return True
        else:
            time.sleep(0.1)
    if raise_exception:
        raise TimeoutError("Condition not fulfilled within timeout. Message: " + msg)
    else:
        return True


def check_if_online():
    try:
        r = requests.get('http://www.google.com')
        return r.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

# if wait_until(check_if_online, timeout=10):
#     print("Connection available")
# else:
#     print("No connection")


def some_function():
    return "Hello"


hello = some_function()

print(hello)

hello_func = some_function

print(hello_func)

print(hello_func())