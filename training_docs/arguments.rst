\*args and \*\*kwargs
==========================

``*args`` and ``**kwargs`` used as arguments in function definition allow to pass variable number of arguments to a function

Consider the example:

.. code-block:: python

    def print_arguments(*args, **kwargs):
        print("Positional arguments")
        for arg in args:
            print(arg)

        print("Keyword arguments")
        for kwarg, value in kwargs.items():
            print("{} = {}".format(kwarg, value))


    print_arguments(1, 2, x=12, y=14, z=['a', 'b', 'c'])

Gives the output:

.. code-block:: none

    Positional arguments
    1
    2
    Keyword arguments
    y = 14
    x = 12
    z = ['a', 'b', 'c']

So, within the function body:

- optional **positional** arguments, marked with \* are represented as a *list*.
- optional **keyword** arguments, marked with \*\* are represented as a *dictionary*.


The names ``args`` and ``kwargs`` are only customary names, optional arguments can be marked with any valid python object name
(``**keywords``, ``**properties``, ``**optional`` etc..)