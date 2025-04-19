.. post:: Jan 01, 2025
   :category: Code
   :tags: Python
   :author: Sam Khalilian
   
Virtual Environments
====================

Virtual environments allow different Python projects to have different package depenedenices e.g.

.. code-block:: python

    DataFrame.sort() # Pandas DataFrame.sort() is deprecated in version 0.20
    DataFrame.sort_values() # Pandas DataFrame.sort_values() in version 0.20
    
A legacy project calling :code:`DataFrame.sort()` can keep usingPandas version < 0.20.

.. note::   
    Since Python 3.3 the venv module has been integrated into the standard library

To create the virutal environemnt where all project package dependencies will be installed:

.. code-block:: bash

    $ cd %PROJECT% # select project directoy
    $ %PYTHONPATH% -m venv .venv # install virtual environment in subdirectory .venv
    $ .venv\Scripts\activate # activate virtual environment

Common

.. code-block:: bash

    $ pip install <PACKAGE> # install packages
    $ pip list # list installed packages in virtual
    $ pip freeze > requirements.txt # output list of installed Python packages and versions to requirements.txt

The virtual environment is shown as active by the prefix (.venv) in the terminal prompt.

.. code-block:: bash
    :caption: terminal

    (.venv) Z:\blog> pip install <PACKAGE> # install packages
    (.venv) Z:\blog> pip list # list installed packages in virtual
    (.venv) Z:\blog> pip freeze > requirements.txt # output list of installed Python packages and versions to requirements.txt
  

..note::
    A best practice is to name the virtual environment .<PACKAGENAME>.
    The '.' differentiates the file from a file not to be released and to be added to .gitignore.
    A standard package name to use in .venv.
