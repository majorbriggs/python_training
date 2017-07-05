.. _magic:

Magic methods
----------------

*Magic methods* are special methods in classes that have names starting and ending with double underscore.

The most commonly used special method is ``__init__()`` called after an instance of a class is created.

Using other special methods you can make your classes behave like dictionaries, sets, functions, iterators, numbers etc.


String representation of a class
++++++++++++++++++++++++++++++++++++++


By defining ``__repr__(self)`` method your class gets a custom representation as a string.

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
But if ``__repr__`` is defined, and ``__str__`` is not, the object will behave as if ``__str__=__repr__``, but not vice versa.

see `stack overflow <https://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python>`_ for more information on differences between theese two.


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
