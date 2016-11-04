Common Python *gotchas*
===========================================

Situations where Python way of doing things is not what we may expect

What exactly are variables in Python?
------------------------------------------------

Let's consider the following piece of code

.. code-block:: python

    first_list = [1, 2, 3]
    second_list = first_list

    second_list.append(4)
    print(first_list) # [1, 2, 3, 4]

    print(l1 is l2) # True
    print(l1 == l2) # True

You might expect to see in the end the original content of the list ``[1, 2, 3]``.

Instead, both ``second_list`` and and ``first_list`` are references to the same list object. Why is it so?

Variables as "labels" of objects
+++++++++++++++++++++++++++++++++++++

If you have any experience from other popular programming languages, you may expect that in statements like:

.. code-block:: python

    x = ["Bob", "Alice"]
    x = 1
    y = x

``x`` and ``y`` would be some places in memory, that upon the execution of these lines get "filled" with the appropriate values (a list, a number and the same number respectively)

But that's is **not** how things work in Python.

``x`` or any variable is only a label, assigned to an object as a reference (to the list ``['Bob', 'Alice']`` in this case) ,
and on the next line, the same "label" is re-assigned to another object - the number ``1``.
Both these objects can have multiple variables assigned to them and may continue to exist even if ``x`` or ``y`` do not refer to them anymore.

In practice these *objects* exist until there is at least one *variable* refering to them. It may be confusing, so let's see another example:


.. code-block:: python

    a = "Bob"
    b = a

``a`` and ``b`` are not separate objects. They are separate "labels" pointing to the same string object ``"Bob"``

.. _fig2vars1obj:

.. figure:: img\objects_1.png
    :align: center

    Both variables are assigned to the same object


Now now reassign the variable ``b`` to another string object ``"Alice"``.

.. code-block:: python

    b = "Alice"

.. _fig2vars2obj:

.. figure:: img\objects_2.png
    :align: center

    Second variable is reassigned to another object.


Let's go back to the original example:

.. code-block:: python

    first_list = [1, 2, 3]
    second_list = first_list

    second_list.append(4)
    print(first_list)

Exactly like in the previous example, both varialbes ``first_list`` and ``second_list`` are assigned to the same object in memory (like in :numref:`fig2vars1obj`)
As list are **mutable** objects, they can be changed "in place". We append a new element to the list that is referenced by both ``first_list`` and ``second_list``, no matter which variable we use in the append method on.

How to create a **real** copy of an object
+++++++++++++++++++++++++++++++++++++++++++++++++++++

To create a copy of an object, separate and independent from the original variable you can use:
:py:func:`copy.copy` and :py:func:`copy.deepcopy`

From python docs:

The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):

- A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
- A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.


alternatively, a copy of a list is often created with slicing

.. code-block:: python

    l1 = [1, 2, 3, 4, 5]

    l2 = l1[:] # returns a "slice" with all elements of l1

    print(l1 is l2) # False
    print(l1 == l2) # True



Mutable default arguments
---------------------------------

The most common and controversial example of an 'unusual' behavior of Python is how default mutable arguments are evaluated.

What are mutable and immutable objects
+++++++++++++++++++++++++++++++++++++++++++

Mutable objects in Python are the ones that can be changed "in place", without assigning it to a new objects.
For example, you can use ``some_list.append('new_element')`` to add a new element to ``some_list``, the method does not return a new list, but changes the original object referenced by ``some_list``.

Immutable:
    - Numeric types: int, float, complex
    - string
    - tuple
    - frozen set
    - bytes

Mutable:
    - list
    - dict
    - set
    - byte array

.. code-block:: python

    i = 10 # mutable, there is no i.increment() method available
    s = 'some text'  # there is no method that would allow you to "mutate" the object itself
    # all methods like string.split() or string.replace() return a *NEW* string
    changed_string = s.replace('some', 'some_other')

    l = [1, 2, 3]
    l.append(4)  # l is still the same object, but mutated (one element longer)


Mutable object as default function argument
+++++++++++++++++++++++++++++++++++++++++++++++

Consider the following function

.. code-block:: python

    def add_vegetable(vegetable, list_of_vegetables=[]):
        list_of_vegetables.append(vegetable)
        return list_of_vegetables

    first_list = add_vegetable('carrot')
    second_list = add_vegetable('banana')

    print(first_list)
    print(second_list)


What you may expect to see is something like:

.. code-block:: none

    ['carrot']
    ['banana']


But instead you get

.. code-block:: none

    ['carrot', 'banana']
    ['carrot', 'banana']


This is because Python evaluates the default values only once, when the function is defined and not each time it is called.
Therefore, all subsequent calls of ``add_vegetables()`` are using the same object, which each time is mutated by the function.

Another important thing to notice here is that we didn't get the following either:

.. code-block:: none

    ['carrot']
    ['carrot', 'banana']


This is because both ``first_list`` and ``second_list`` are not separate objects, they are only
"tags" that point to the same object in the memory (the default argument of ``add_vegetables``)
therefore, when the default list_of_vegetables is changed, each variable that "points" to this object will return the changed value


What should be done to get the expected behavior is

.. code-block:: python

    def add_vegetable_correctly(vegetable, list_of_vegetables=None):
        if list_of_vegetables is None:
            list_of_vegetables = []
        list_of_vegetables.append(vegetable)
        return list_of_vegetables

    first_list = add_vegetable_correctly('carrot')
    second_list = add_vegetable_correctly('banana')

    print(first_list)
    print(second_list)

This time we really get

.. code-block:: none

    ['carrot']
    ['banana']


The general rules are:

#. Don't use mutables (strings or lists) as default arguments
#. Unless you have a good reason to
#. In all other cases, use ``None``, check for it and create the empty list or string inside the body of the function

Read more on `Python Conquers The Universe <https://pythonconquerstheuniverse.wordpress.com/2012/02/15/mutable-default-arguments/>`_



Boolean expressions and logical operators
-----------------------------------------------

Boolean operations do not return only True or False values. To get the concept, let's consider what Python considers to by a "truth".

Testing for Truth value
++++++++++++++++++++++++++++

In python, every object can have a "truth" value assigned and therefore be used in ``if`` statements, ``while`` loops and boolean operations:

The values considered false are:
    - ``None``
    - ``False``
    - Zero of any numeric type (int, float, complex)
    - Empty sequences (lists, tuples, sets)
    - Empty dicts
    - instances of user-defined classes, if the class defines a ``__nonzero__()`` or ``__len__()`` method, when that method returns the integer zero or bool value False

All other values are considered true.

That is why it's possible (and also considered to be a good practice) to use this language feature in the truth tests like so:

.. code-block:: python

    some_string = ''

    if some_string:
        print('The string is not empty')

Instead of testing the condition explicitly, which is in this case superfluous.

.. code-block:: python

    some_string = ''
    if some_string != '':
        print('The string is not empty')

``and`` and ``or`` operators
++++++++++++++++++++++++++++++++++

Python offers a useful, but somehow specific evaluation of the boolean ``and`` and ``or`` boolean operators

Consider the following example:

.. code-block:: python

    x = 1
    y = []
    x or y  # returns 1
    x and y # returns []
    y or x # returns 1

In general ``or`` and ``and`` do **not** return ``True`` or ``False``, but the value of the last evaluated element.

which means in particular (from `Python Docs <https://docs.python.org/3.5/library/stdtypes.html#boolean-operations-and-or-not>`_)

========== ========================================= =========================
Operation  Result                                    Notes
========== ========================================= =========================
x or y     if x is false, then y, else x             `(1)`
x and y    if x is false, then x, else y             `(2)`
not x      if x is false, then True, else False      `(3)`
========== ========================================= =========================

Notes:

#. This is a short-circuit operator, so it only evaluates the second argument if the first one is False.
#. This is a short-circuit operator, so it only evaluates the second argument if the first one is True.
#. not has a lower priority than non-Boolean operators, so not a == b is interpreted as not (a == b), and a == not b is a syntax error.

This pattern can be used as a shortcut when setting default values

.. code-block:: python

    default_list = [1, 2, 3, 4, 5]

    some_other_list = []

    new_list = some_other_list or default_list

    print(new_list is default_list) # -> True