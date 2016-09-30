Environment configuration
===========================================

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


Installing packages into the virtual environment
+++++++++++++++++++++++++++++++++++++++++++++++++

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

pip
-----

:py:mod:`pip` is the recommended tool for installing packages from `Python Package Index <http://pypi.python.org/>`_. PyPI is a repository for open-source third-party Python packages.
From version 3.4 :py:mod:`pip` is a standard element of python installations.

See `pip documentation <https://pip.pypa.io/en/stable/>`_ for more.

The basic command to install a package is:

.. code-block:: bat

    python -m pip install name_of_the_package

You can also:

.. code-block:: bat

    python -m pip uninstall name_of_the_package

or:

.. code-block:: bat

    python -m pip install --upgrade name_of_the_package

PyCharm also uses pip to install additional packages in the Project Interpeter settings window.

requirements.txt file
++++++++++++++++++++++++++

Requirements files (typically :file:`requirements.txt`) are files containing a list of items to be installed using pip.

They allow you to create repeatable configuration, that can be shared with other developers working on the project.
To install all requirements listed in the file use:

.. code-block:: bat

    python -m pip install -r requirements.txt


The file can be created with the freeze command like so:

.. code-block:: bat

    python -m pip freeze > requirements.txt
    python -m pip install -r requirements.txt


See `Requirements Files Format <https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format>`_ for details on the syntax.

