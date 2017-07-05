Decorators
========================

Decorators allow to dynamically extend the behavior of a function or functions they are applied to, without the need to
modify the function itself. To understand how they are implemented in Python, let's start with some introductory concepts.

Functions are objects
--------------------------

Everything is an object in Python, even types like int, str, or *functions* are objects. We will concentrate now on consequences of the latter.

It is often said that functions are **first class objects** in Python, which means that there are no restrictions on their usage as objects.
As such, they can be created, destroyed, passed as an argument or returned by another function with a :py:keyword:`return` statement.

Let's consider the following example:


.. code-block:: python

    class Animal():
        def __init__(self, name, make_sound_method):
            self.name = name
            self.make_sound = make_sound_method


        def quack():
            print('Quack!')


        def moo():
            print('Moooo!')


        def bah():
            print('Bah!')


    bah = Animal(name='Sheep', make_sound_method=bah)

    bah.make_sound()

.. hint::

    The above is an example of **Strategy** design pattern. In this pattern:

    - there is a set of predefined algorithms (here different sound methods, ``moo``, ``quack``, ``bah``)
    - the object has a "placeholder" field - a method in its interface, that can execute different algoritms (here ``make_sound()``,
    - The algorithm that is used on call of the method is selected from the set of predefined algorithms on runtime.

As you see, any function can be used as an object (for example to assign it to some other variable), by refering to it without the parentheses ().

Please consider the differences in the following calls:

.. code-block:: python

    def some_function():
        return "Hello"


    hello = some_function()
    hello_func = some_function

    print(hello)
    # -> Hello

    print(hello_func)
    # -> <function some_function at 0x01290DF8>

    print(hello_func())
    # -> Hello


Excercise: DEC00: Implement a simple strategy pattern
-------------------------------------------------------

Following the example above, implement a simple class that will realize the Strategy pattern.

Write three functions that will simulate different processing algorithms (they can all be a single print() statement)
The class should have one method "process" which will be initiated with one of the three possible algorithms


Excercise: DEC01: Functions are objects - ``wait_until`` method
---------------------------------------------------------------

To see some real benefit from passing functions as arguments to other functions, let's implement a custom ``wait_until()`` function that will check a given condition until timeout is expired.

Tasks
++++++++

Write an implementation of a wait_until function according to the following docstring.

.. code-block:: python

    def wait_until(condition, timeout=10, raise_exception=True, msg=""):
        """Wait until the condition returned by 'condition' function is fulfilled,
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

.. hint::

    Use the method :py:func:`time.time` to get the current time.
    To simulate a condition function that is fulfilled after some time use :py:func:`time.sleep`


:ref:`DEC01_solution`


Functions defined within another function
----------------------------------------------

Python allows you to define a function within another function:

.. code-block:: python

    def outer_function(filter):

        def inner_function():
            print("Inside inner function")

        inner_function()

This can be used e.g. for a better code isolation (the inner function has a limited scope) or to create decorators.

Function decorators
------------------------

A function decorator is a wrapper that modifies the behavior of the wrapped function, e.g. by adding some additional
code before and after the function's execution. The decorator does not require any modifications to the existing code.

A practical example may be logging of the code execution or checking some additional requirements before / after the function is executed.

.. code-block:: python


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
    def test_step_1():
        print("Do something")


Stacked decorators
+++++++++++++++++++++

Decorators can be also stacked.

.. code-block:: python

    @teststep
    @requires_login
    def some_test_step():
        print("Hi!")


Decorators with parameters
++++++++++++++++++++++++++++++++

But...

.. image:: img\deeper.jpg

Behavior of decorators can also be modified by parameters.
To create such a parameterized decorator, create another function that wraps the decorator and accepts some parameter.

Consider the example:

.. code-block:: python


    def outer_decorator(some_parameter):
        def real_decorator(func):
            def wrapper(*args, **kwargs):
                # inner function uses the parameter from the outer-most function
                print("Decorator got the parameter: {}".format(some_parameter))
                print("Decorated function starts")
                result = func(*args, **kwargs)
                print("Decorated function finished.")
                return result
            return wrapper
        return real_decorator


    @outer_decorator("Some parameter")
    def test_step():
        print("Do something")


    test_step()





Excercise: DEC02: Function decorator with parameters
---------------------------------------------------------------

Write a decorator, that will enclose the string returned by the decorated function with html tags.
The decorator will use a parameter, so this requries a a 3-level structure like in the example above.

The execution of ``greet`` function decorated like this:

.. code-block:: python

    @tags('div')
    @tags('p')
    @tags('span')
    def greet(name):
        return "Hello " + name

    print(greet("My Friend"))

should return the string:

``<div><p><span>Hello My Friend</span></p></div>``


:ref:`DEC02_solution`
