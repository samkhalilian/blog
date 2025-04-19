.. post:: Jan 01, 2025
   :category: Code
   :tags: Python
   :author: Sam Khalilian

Python Install Package
======================

Python Install Package (PIP) is a package manager for Python enabling installation of Python packages (modules).

.. note::
    PIP is included by default with Python version 3.4 or later. 

A list of packages available to install can be found at `PyPI <https://pypi.org/>`_.

===============
Useful commands
===============

.. code-block:: bash

    $ pip install <PACKAGE> # install package
    $ pip install <PACKAGE> --upgrade # upgrade package
    $ pip uninstall <PACKAGE> # uninstall package
    $ pip list # list installed packages

====
.whl
====

Sometimes pacakges maybe available for installation instead from file wheel format (.whl).  

This is a built-package format for Python that can be installed using PIP.

.. code-block::

    $ pip install <PATH> # install package from wheel file

================
requirements.txt
================

    *"Requirements files serve as a list of items to be installed by pip, when using pip install. 
    Files that use this format are often called “pip requirements.txt files”, since requirements.txt is usually what these files 
    are named (although, that is not a requirement)."*

    --- https://pip.pypa.io/en/stable/

.. code-block::

   $ pip freeze > requirements.txt # output list of installed Python packages and versions
   $ pip install -r requirements.txt # install packages from requirements.txt
