Sam's Blog
==========

============
Introduction
============

Welcome to my Math, Coding and Trading blog!

This blog is written using `ABlog <https://ablog.readthedocs.io>`_ an extension to `Sphinx <https://www.sphinx-doc.orgl>`_.

The pages are hosted on a `Google Cloud Platform <https://cloud.google.com/storage/docs/hosting-static-website>`_ static website `Sam's Blog <www.samkhalilian.co.uk>`_.

===========
Quick Start
===========

To build the blogs HTML pages install `Python 3.6 <https://www.python.org/downloads/>`_ or higher, then from the command line:

.. code-block:: bash
    
    # optional environment variables
    >> set PYTHON = %LOCALAPPDATA%\Programs\Python\Python310\python
    >> set HOME = %HOMEDIR%%HOMEPATH%  # set home directoy
    >> set PROJECT = %HOME%/project  # select project directoy
    
    >> cd %PROJECT%
    >> git clone https://github.com/samkhalilian/blog.git

    # virtual environment
    >> cd blog
    >> %PYTHON% -m venv .venv 
    >> .venv\Scripts\activate

    # install packages (to be superseded by setup.py)
    >> pip install ablog # install https://ablog.readthedocs.io/
    >> pip install Pallets-Sphinx-Themes # install theme

    # build blog pages
    >> cd ./blog/src
    >> ablog clean
    >> ablog build # build HTML pages
    >> ablog serve # to launch HTML pages
