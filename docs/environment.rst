Environment configuration
===========================================

We start with setting up a development environment, installation of third part libraries and virtual environments.


Setting environment variables
---------------------------------

In case you have multiple versions of python installed alongside, make sure you know which interpreter is started by ``python`` command.

On Linux systems, where both versions of Python are pre-installed by default, ``python`` command starts the system Python2.x and ``python3`` the 3.x version respectively.

By default, the python directory should be added to the system ``PATH`` variable.
Test it by running command line and typing ``python``


.. tip::

    If you have both 2.x and 3.x installed, you can choose the version to run by typing:

    - ``py -2`` for Python 2.x
    - ``py -3`` for Python 3.x


If after typing ``python`` in the command line, you get the error:

.. code-block:: none

    'python' is not recognized as an internal or external command, operable program or batch file.

add to the user or system ``PATH`` variable the correct paths to Python and Python\\Scripts directories (e.g. ``C:\Python35-32\Scripts\;C:\Python35-32\``)



pip
-----

:py:mod:`pip` is the recommended tool for installing packages from `Python Package Index <http://pypi.python.org/>`_. PyPI is a repository for open-source third-party Python packages.
From version 3.4 :py:mod:`pip` is a standard element of python installations.

See `pip documentation <https://pip.pypa.io/en/stable/>`_ for more.



pip with SSL certificates
++++++++++++++++++++++++++++++

If your network requires you to use a certificate for SSL connections, create a folder
``pip`` in your user directory, e.g. ``C:\Users\YourUsername\pip``

and create there a file ``pip.ini`` specifying the path to the certificate:


.. code-block:: bat

    [global]
    cert = C:\Users\YourUsername\pip\certificate.pem



Installing packages with pip
+++++++++++++++++++++++++++++++++

The basic command to install a package from pip is:

.. code-block:: bat

    pip3 install name_of_the_package

You can also:

.. code-block:: bat

    pip3 uninstall name_of_the_package

or:

.. code-block:: bat

    pip3 install --upgrade name_of_the_package

Use ``pip`` for Python2.x (if Python2 is installed and its directory is in PATH)


PyCharm also uses pip to install additional packages in the Project Interpeter settings window.

.. tip::
    If ``pip3`` is not recognized in by your command line, add the ``Scripts`` directory (by default ``C:\Python35-32\Scripts``) to your ``PATH`` or use ``py -3 -m pip`` instead

pip in virtual environments
+++++++++++++++++++++++++++++++++

To install libraries in a selected virtualenv only, you must activate it first with ``{venv_directory}\\Scripts\\activate.bat``

requirements.txt file
++++++++++++++++++++++++++

Requirements files (typically :file:`requirements.txt`) are files containing a list of items to be installed using pip.

They allow you to create repeatable configuration, that can be shared with other developers working on the project.
To install all requirements listed in the file use:

.. code-block:: bat

    pip3 install -r requirements.txt


The file can be created with the freeze command like so:

.. code-block:: bat

    pip3 freeze > requirements.txt
    pip3 install -r requirements.txt


See `Requirements Files Format <https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format>`_ for details on the syntax.





PyCharm Git setup
-------------------
- Create a new Git repostory for the project files on GitHub or `LHSY GitBucket <http://git.dev.lsy.pl>`_
- Start PyCharm
- Go to VCS -> Check out from Version Control -> Git
- Enter the repository URL and click Clone
- create a file :file:`.gitignore` and put there the following line (directory containing the PyCharm project settings)

.. code-block:: bat

    .idea


virtualenv
-----------------------

:py:mod:`virtualenv` is a tool to create isolated Python environments.
It creates an environment that has its own installation directories,
that doesn’t share libraries with other virtualenv environments
(and optionally doesn’t access the globally installed libraries either).

See `virtualenv documentation <https://virtualenv.pypa.io/en/stable/>`_ for more.

Why do we need virtual environments
++++++++++++++++++++++++++++++++++++++

Virtualenv allows multiple Python projects that have different (and often conflicting) requirements, to coexist on the same computer.
It also helps you to keep a track on what third-part libraries are needed for the project to run
(especially when used with :file:`requirements.txt` files described below)

PyCharm Setup
++++++++++++++++++++++++++++++++++++++

#. Go to File -> Settings -> Project -> Project Interpeter -> Gear Icon -> Create VirtualEnv
#. Select Python 3.5.x interpreter, give it a meaningful name and click OK

.. image:: img\create_venv.png


Installing packages into the virtual environment with PyCharm
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- While in Project Interpreter Settings, click +, search for "requests" and click Install Package
- Create a new file and type:

.. code-block:: python

    import requests

- See that the import to the newly installed library is correctly resolved

Working with virtualenv outside of IDE
++++++++++++++++++++++++++++++++++++++++++



- Go to the location of your new virtual environment and open the command window there (Shift+Right click -> Open command window here)

.. image:: img\run_cmd_here.png

- run

.. code-block:: bat

    Scripts\activate.bat

.. image:: img\activate_venv.png

- the name of the virtual environment (training_venv in this case) displayed before your working directory indicates that the environment is active.
- run python and import the library that is installed in this environment (:py:mod:`requests`)
- type deactivate to return to the standard environment
