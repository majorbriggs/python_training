Creating documentation with :py:mod:`Sphinx`
=============================================

The documentation of this training was created with :py:mod:Sphinx which is the standard used for Python docs.

In this introduction we will create a simple docs and analyze the sources of this documentation.


Installation & project template
--------------------------------------------

#. Install Sphinx with ``pip3 install Sphinx``
#. Create an empty project by typing ``sphinx-quickstart``
#. Say yes to the “autodoc” extension, use defaults for all other questions
#. Open the docs folder in pyCharm, install reStructuredText extension for PyCharm.

reStructuredText
--------------------

`reStructuredText <http://docutils.sourceforge.net/rst.html>`_ is the markup syntax used by Sphinx.
See the official documentation for an overview of the syntax.


Creating Sub-pages
----------------------

To create a sub page and add it to the Table of Contents:

- Add a new .rst file with any name (e.g. ``subpage.rst``)
- Open ``index.rst`` and add the newly created page under the ``.. toctree: section`` (see below). Remember that in reST, the indentation (tabs and spaces) is also a part of the syntax.

.. code-block:: rst

    Contents:

    .. toctree::
       :maxdepth: 2

       subpage

- Open ``subpage.rst`` and add a new section title by writing


.. code-block:: rst

    Title of the subpage
    =========================

    This is the content of the section


Building HTML
-------------------------------

- Go to the docs sources directory, open command line there and type ``make html``
- Open the resulting docs HTML in ``_build\html\index.html``


Excercise DOC00: Analyze the training docs sources
-------------------------------------------------------

#. In PyCharm, clone the training repository https://github.com/majorbriggs/python_training.git
#. Analyze how the different sections of the docs were defined in the corresponding reST documents.
#. Check how references to external documentations (e.g. to :py:mod:`requests`) are resolved thanks to ``intersphinx_mapping`` setting in ``conf.py``
#. Check how different language highlighting works on examples from requests.rst (php, python, none, rst)