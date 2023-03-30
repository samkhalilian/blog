Virtual Environments
====================

Virtual environments allow different Python projects to have different package depenedenices.

E.g. the Pandas DataFrame.sort() method is deprecated as of version 0.20 and is replaced by DataFrame.sort_values() and 
DataFrame.sort_index().  Where a legacy project is using version 0.16 and calls DataFrame.sort_values() it can not use version
0.20 or higer.

Best practice is to name the virtual environment .venv_<PROJECT> to a create unique virtual environment.
The '.' differentiates the file from a file not to be released and to be added to .gitignore.

To create the virutal environemnt where all project package dependencies will be installed:

.. code-block:: bash

    >> cd %DIR_PROJECT% # select project directoy
    >> %USERPROFILE%\AppData\Local\Programs\Python\Python310\python -m venv .venv # create directory .venv
    >> .venv\Scripts\activate # activate .venv