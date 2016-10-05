Regular expressions
=========================


Introductions
---------------------------


Useful tips
---------------------------

Use ``groups()`` and unpacking to get multiple parts of the match
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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

Python online checker
+++++++++++++++++++++++

Use `Regex101 <https://regex101.com/>`_ for regex debugging. (with Python specific interpreter)