Classes and Object Oriented Programming
===========================================

Classes and objects are the two main aspects of object oriented programming. In Python, everything is an object - even things
like ints, and strings which in some other languages are called primitives.

In Python (unlike in Java) multiple classes can be defined within one file on the same level.
Classes can be defined within other classes or even within functions.


Declaration of a simple class

.. code-block:: python

    class Employee:

        def __init__(self, name, salary):
            self.name = name
            self.salary = salary


        def get_salary_after_tax(self):
            return self.salary * 0.71

    emp = Employee("Joe", 10000)


    print(emp.name)
    print(emp.salary)

    print(emp.get_salary_after_tax())


.. hint::

    Python does not have typical access modifiers like **private** **public** or **protected**. All members of a class can be
    accessed, the responsibility to use them wisely lies on the developer. However, special naming conventions are used to indicate
    members that should be used only within the class or package (by using ``_`` as a prefix for protected and ``__`` for private members)

    While using 3rd party libraries, you should definitely avoid accessing members with _ prefix, as they are not part of the API and may be changed in the future.
    This doesn't apply to special methods like __str__ __class__ (see :ref:`magic`)



The ``self`` argument
---------------------------------------------------------------------------

``self`` as the first argument of each method in a class represents the instance of the class
This instance is automatically passed to the method during the call.
``self`` is used to access any members of the instance from within the method.



Bonus: ``@classmethod`` and ``@staticmethod``
--------------------------------------------

This is a larger topic, but just to give you a glimpse

``@staticmethod``
Methods decorated as staticmethods do not know anything about the class of instance they are called on, they do not operate on
the fields of the class


``@classmethod``
Instead of the instance of the class (``self``), these methods get the **class** itself as the first parameter.
They have access to class members via ``cls`` argument.

.. code-block:: python

    class Employee:

        def __init__(self, name, salary):
            self.name = name
            self.salary = salary


        def get_salary_after_tax(self):
            return self.salary * 0.71 #  this needs self to access instance members

        @staticmethod
        def this_does_not_have_self(a, b):  # this method belongs to the class, but do not have access to instance or class fields
            print(a + b)


        @classmethod
        def this_method_gets_the_class_and_not_the_instance(cls):
            print("This is a classmethod of class {}".format(cls))