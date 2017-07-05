Built-in types - good practices
=====================================

Assuming that all of you have the basic knowledge about built in types, we will only concentrate on some "good practices" and typical idiomatic expressions.

Iterating over a list
--------------------------


Always use:

    .. code-block:: python

        for item in some_list:
            print(item)

Instead of:

    .. code-block:: python

        for i in range(len(some_list)):
            print(some_list[i])

If you want to use both the index, and the value, use ``enumerate()`` with unpacking

    .. code-block:: python

        for index, value in enumerate(some_list):
            print("Value on index {0} is {1}".format(index, value))


If you want to iterate over the items of two lists at the same time, use ``zip()`` (like in a zipper)

    .. code-block:: python

        A = [1, 2, 3]
        B = ['a', 'b', 'c']


        for a, b in zip(A, B):
            print("A: {} B: {}".format(a, b))



Creating a dictionary from two lists
----------------------------------------------------

You can use the same ``zip()`` function to quickly create a dictionary from two lists, one containing the keys, and the other the values.


.. code-block:: python

    keys = [1, 2, 3]
    values = ['a', 'b', 'c']

    d = dict(zip(keys, values))
    # -> {1: 'a', 2: 'b', 3: 'c'}

.. hint::

    A better way to create a dictionary of all letters with their corresponding number, would be to ``enumerate()`` the ``asci_lowercase`` string constant:

    .. code-block:: python

        from string import ascii_lowercase

        d = dict(enumerate(ascii_lowercase))


Iterating over a dictionary
----------------------------------------------------

The standard and "pythonic" way to iterate over all items of a dictionary, if we intend to use both keys and values is with the method ``items()``


.. code-block:: python

    dictionary = {"first_name":"Bob",
        "last_name":"der Baumeister"
        "occupation":"builder"}

    for key, value in d.items():
        print("Value of {} is {}".format(key, value))


For a contrast, some other possible ways, that should **not** be used due to their obscurity:

.. code-block:: python

    for key in dictionary:
        print("Value of {} is {}".format(key, dictionary[key]))


    for element in dictionary.items():
        print("Value of {} is {}".format(element[0], element[1]))
