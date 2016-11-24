Advanced concepts
========================


Magic methods in classes
---------------------------------

*Magic methods* are special methods in classes that have names starting and ending with double underscore.

The most commonly used special method is ``__init__()`` called after an instance of a class is created.

Using other special methods you can make your classes behave like dictionaries, sets, functions, iterators, numbers etc.

String representation of a class
++++++++++++++++++++++++++++++++++++++


By defining ``__repr__()`` method your class gets an official custom representation as a string.

.. code-block:: python

    class MyClassWithRepr():
        def __init__(self):
            pass

        def __repr__(self):
            return "This is my class"

    class MyClassWithoutRepr():

        def __init__(self):
            pass


    x = MyClassWithoutRepr()

    y = MyClassWithRepr()

    print(x)
    # -> <__main__.MyClassWithoutRepr object at 0x00B5A530>

    print(y)
    # -> This is my class

Additionally, there is also a  ``__str__()`` method which called when you print the object or execute ``str(obj)``.
But if ``__repr__`` is defined, and ``__str__`` is not, the object will behave as if ``__str__=__repr__``


Operator overloading
+++++++++++++++++++++++++++++++++++

By overriding the special methods you can also allow the objects of your classes to be added, subtracted, devided or compared.
Consider the example below, keeping in mind that there are probably better ways to work with vectors and matrices in Python than DIY classes like this one. (like |nbsp| :py:mod:`numpy`)

.. code-block:: python

    class Vector1D():

        def __init__(self, *args):
            for arg in args:
                if not isinstance(arg, int):
                    raise ValueError("Vector1D can store only integer values")

            self._values = args

        def __str__(self):
            return self._values

        def __add__(self, other): # + operator
            if not isinstance(other, Vector1D):
                raise ValueError('Expected Vector1D, instead got {}'.format(other.__class__))

            if len(self._values) != len(other._values):
                raise ValueError('Added vectors have to have the same lenght')

            return [i + j for i, j in zip(self._values, other._values)]

        def __eq__(self, other): # == operator
            return self._values == other._values # != operator

        def __ne__(self, other):
            return self._values != other._values

    A = Vector1D(1, 2, 3, 4)

    B = Vector1D(5, 6, 7, 8)

    C = A + B

    print(A == B) # -> False

    print(C)
    # -> [6, 8, 10, 12]


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

To make it clear:

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


Excercise: ADV00: Functions are objects - ``wait_until`` method
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

:ref:`ADV00_solution`
