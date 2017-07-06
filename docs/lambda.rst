Lambda expressions
========================

:py:keyword:`lambda` keyword allows to create small anonymous functions. They are restricted to be a single expression.
The following function definition:

.. code-block:: python

    def sum(a, b):
        return a + b


Has the corresponding representation as an anonymous function

.. code-block:: python

    lambda a, b: a + b

So, everything that comes after the colon, is **returned** by the anonymous function.
The names before the colon, separated with a coma represent arguments that are passed to the function.

Lambda expressions can be useful whenever we need a callable function argument.
For example, in GUI programming - lambdas are used to create callbacks e.g. for button clicks:

.. code-block:: python

    # (...)

    frame = tk.Frame(parent)
    frame.pack()

    btn = tk.Button(frame, text="22", command=lambda: self.printNum(22))

In the example above, the argument passed as ``command`` needs to be a callable object.

An alternative implementation, that doesn't use lambda, looks like this:

    # (...)

    frame = tk.Frame(parent)
    frame.pack()

    def print_num_22():
        return self.printNum(22)

    btn = tk.Button(frame, text="22", command=print_num_22) # command must be a callable object



Lambda expressions in test automation
-------------------------------------------

In our test automation frameworks, we are using lambda expressions for conditions that must be checked periodically
(e.g. waiting for an element to appear in a table)

.. code-block:: python

    assertion(callable_condition=lambda: self.ui_table().get_row_count() == count,
                msg=f'Agency User List should have {count} rows')

The assertion function would have an implementation similar to:

.. code-block:: python

    import time

    def assertion(callable_condition, msg, number_of_retries=10):
        for i in range(number_of_retries):
            if callable_condition():
                return True
            else:
                time.sleep(1)
        raise AssertionError(msg)s