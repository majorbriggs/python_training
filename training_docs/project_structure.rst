Project structure
===========================================

Modules
-------------------------------------

A module is a file containing Python code. A a module can be imported into other modules with the :py:keyword:`import`
The module name is available within the module as a :py:data:`__main__`

The ``if __name__ == '__main__'`` section
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

You will often see the main part of a script enclosed in such if block.

**TL;DR** If you skip this part and write some code directly on the top level of the module (not inside a function),
the code will be executed every time you import your module from somewhere else.


.. code-block:: python

    if __name__ == '__main__':
        print('This is executed only if the module is executed directly by python interpreter')



Detailed explanation
____________________

From the best `stackoverflow answer <http://stackoverflow.com/questions/419163/what-does-if-name-main-do>`_ on this question:

When the Python interpreter reads a source file, it executes all of the code found in it.
Before executing the code, it will define a few special variables.
For example, if the python interpreter is running that module (the source file) as the main program,
it sets the special __name__ variable to have a value "__main__".
If this file is being imported from another module, __name__ will be set to the module's name.


That means, that the code in this block is executed only, if the module is run directly by the interpeter (and not imported into another module)

.. code-block:: bat

    python my_module.py

and is skipped, when the module is imported

.. code-block:: python

    import my_module


Packages
----------

Packages allow you to structure your project and access the modules using a dot . notation

example:

.. code-block:: python

    from my_package.my_module import my_function


If you want Python to treat a directory as a package (collection of modules or sub-packages),
it must contain an :file:`__init__.py` file.
The file can be (and very often is) empty, but it can also contain some initialization code,
that will be executed on the first import of the package

example package/directory structure (from `python docs <https://docs.python.org/3/tutorial/modules.html#packages>`_)

.. code-block:: none

    sound/                          Top-level package
          __init__.py               Initialize the sound package
          formats/                  Subpackage for file format conversions
                  __init__.py
                  wavread.py
                  wavwrite.py
                  aiffread.py
                  aiffwrite.py
                  auread.py
                  auwrite.py
                  ...
          effects/                  Subpackage for sound effects
                  __init__.py
                  echo.py
                  surround.py
                  reverse.py
                  ...
          filters/                  Subpackage for filters
                  __init__.py
                  equalizer.py
                  vocoder.py
                  karaoke.py
                  ...


Importing rules
------------------

There are multiple ways of importing packages, modules and objects

.. code-block:: python

    import math

    print(math.sin(1))

.. code-block:: python

    from math import sin

    print(sin(1))

.. code-block:: python

    from math import * #  NOT recommended - it will pollute your namespace with objects that you may not need
    # possibly overwriting the necessary stuff
    print(sin(1))


.. code-block:: python

    from object import module as some_other_name

    some_other_name.some_function()


Circular imports
-------------------

Imagine a situation where the module A.module_one imports the module B.module_two which itself imports some object or module from A.
This is called a Circular import and, even if in some cases executable,
should be avoided by refactoring the module/packages structure e.g. into smaller, independent pieces.

A non-resolvable circular import may be indicated by the error message:

.. code-block:: none

    ImportError: cannot import name 'some_object'
