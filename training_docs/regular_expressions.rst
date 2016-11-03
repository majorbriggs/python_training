Regular expressions
=========================


Introduction
---------------------------


Compiled regular expressions vs module-level functions
------------------------------------------------------

You can use most of the regex operations in two ways

- as module-level functions of :py:mod:`re` module

.. code-block:: python

    def find_matching_message(pattern, list_of_messages):
        for message in list_of_messages:
            if re.search(pattern, message):  # re.search will compile the regex on each iteration
                return message

- or methods on `compiled regular expression objects <https://docs.python.org/3.5/library/re.html#regular-expression-objects>`_ created with :py:func:`re.compile`

.. code-block:: python

    def find_matching_message(pattern, list_of_messages):
        my_regex = re.compile(pattern)
        for message in list_of_messages:
            if my_regex.search(message):
                return message

For the sake of clarity and also some performance advantage, if the regex is going to be used multiple times,
the second method (compile) is preferred.


.. tip::

    Use `Regex101 <https://regex101.com/>`_ for debugging and testing regular expressions. (It offers a Python specific interpreter)



Using ``groups()`` and unpacking to get multiple parts of the match
------------------------------------------------------------------------

Assume that you have to process messages of the following structure

.. code-block:: none

    @Title: End of the world
    @Event Type: Natural disaster
    @Date: 21-12-2012
    @Details: World is going to end
    @Others: All participants are asked to stay calm and relax

To collect all the parts of the messages and save them in separate python variables, you can do the following

.. code-block:: python

    import re
    message = get_message()  # some message to process
    message_pattern = re.compile('@Title: (.*)\n@Event Type: (.*)\n@Date: (.*)\n@Details: (.*)\n@Others: (.*)')
    title, event_type, date, details, others = message_pattern.search(message).groups()

You can also access them separately with

.. code-block:: python

    title = message_pattern.search(message).group(1)  # group indexing starts from 1


Using :py:func:`re.findall` to get a list of all matches
-----------------------------------------------------------------


:py:func:`re.findall` returns a list of all matches within the string (does not stop on the first one).
If the pattern has more groups, it returns a list of tuples with each tuple containing the groups of the given match.



.. seealso::

    For a more detailed introduction, read the excellent chapter on Python regular expressions in
    `Automate the Boring Stuff with Python <https://automatetheboringstuff.com/chapter7/>`_