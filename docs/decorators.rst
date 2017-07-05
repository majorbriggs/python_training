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
---------------------------------------------------

Following the example above, implement a simple class that will realize the Strategy pattern.

Write three functions that will simulate different processing algorithms (they can all be a single print() statement)
The class should have one method "process" which will be initiated with one of the three possible algorithms


Excercise: DEC01: Functions are objects - ``wait_until`` method
---------------------------------------------------------------

To see some real benefit from passing functions as arguments to other functions, let's implement a custom ``wait_until()`` function that will check a given condition until timeout is expired.

Tasks
++++++++

Write an implementation of a wait_until function according to the following docstring

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

:ref:`DEC01_solution`
