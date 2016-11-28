Working with files
===========================================

Many of your future application will involve some read/write operations on external files.
Python comes with a lot of convenient tool to handle these.

Opening a file
--------------------------

Python has a built in function :py:func:`open` that allows you to create a file object like:

.. code-block:: python

    f = open('some_file.txt')

By default, the file is open in read mode AND has to be closed after usage with

.. code-block:: python

    f.close()


It is good practice to use the :py:keyword:`with` keyword when using file objects. This has the advantage that the file is properly closed after its suite finishes, even if an exception is raised on the way.

.. code-block:: python

    with open('some_file.txt') as f_in:
        x = f_in.read()
        # do some operations

    # no need for f_in.close() statement, it's executed automatically on leaving 'the' with block


Arguments of ``open()`` function
+++++++++++++++++++++++++++++++++++++++

The first argument is a string containing the filename.
The second argument is another string containing a few characters describing the way in which the file will be used.


- ``'r'`` when the file will only be read
- ``'w'`` for only writing (an existing file with the same name will be erased)
- ``'a'`` opens the file for appending; any data written to the file is automatically added to the end.
- ``'r+'`` opens the file for both reading and writing

if the argument is ommited, 'r' is assumed

Normally, files are opened in text mode, that means, you read and write strings from and to the file, which are encoded in a specific encoding. If encoding is not specified, the default is platform dependent

``'b'`` appended to the mode opens the file in binary mode: now the data is read and written in the form of bytes objects. This mode should be used for all files that don’t contain text.

Files can be opened in different modes


Opening multiple files at once
--------------------------------

With "with" you can also open mulitple files at once, by separating the function calls with a coma. It's an easy way to do file processing (reading from one file, writing to another)


.. code-block:: python

    txt = 'some text'
    with open(newfile, 'w') as outfile, open(oldfile, 'r', encoding='utf-8') as infile:
        for line in infile:
            if line.startswith(txt):
                line = line[0:len(txt)] + ' - Truly a great person!\n'
            outfile.write(line)


See :ref:`FIL00` for a short excercise

Working with paths
-----------------------

File operations often require some manipulation of disk paths to create the path string to the required input or output file.
In such cases, the module :py:mod:`os.path` comes in handy. Here are some functions that you might see in use more than often.

:py:func:`os.path.join`: creates a correct path string from a list of strings.The path created with :py:func:`os.path.join` will work regardless the operating system. (On Windows paths are created with ``'\'`` while on Linux with ``'/'``

:py:func:`os.path.abspath` returns the absolute path of a file given with a relative path

:py:func:`os.path.dirname` returns the path to directory of a filename given as argument


Iterating over a file
---------------------------

Use ``for`` loop to iterate over the lines of a file:

.. code-block:: python

    with open('input.txt') as f:
        for line in f:
            if "some string" in line:
                print(line)


.. _FIL00:

Excercise FIL00: Read/write to a file
----------------------------------------

#. Write a script that will write 10 random integers from range 1-10 to a file. Use :py:func:`random.randint` to generate the numbers
#. Open two files (input, output) in a single ``with`` block. Read the numbers from the input file and write the letter ``'X'`` repeated the given number to the output file.

.. code-block:: none

    input.txt

    1
    4
    3

The output file should look like:

.. code-block:: none

    output.txt

    X
    XXXX
    XXX

:ref:`FIL00_solution`
