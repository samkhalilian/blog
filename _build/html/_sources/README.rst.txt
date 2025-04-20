Learn to Code Documentation
===========================

To build the HTML pages install `Python 3.6 <https://www.python.org/downloads/>`_ or higher, then from the command line:

.. code-block:: bash
    
    $ cd %PROJECT% # project directory
    $ git clone https://github.com/samkhalilian/blog.git

    # virtual environment
    $ cd blog
    $ %PYTHON% -m venv .venv # python.exe path
    $ .venv\Scripts\activate
    
    # install packages
    $ pip install -r requirements.txt
    
    # build pages
    $ rmdir /s build
    $ sphinx-build -M html source build -v -E --force # create HTML pages in build\html
    
    $ start "" build\html\index.html # open in browser
    
    $ python -m http.server -d build/html # serve on localhost:8000
    $ start http://localhost:8000/index.html # open in browser

    $ sphinx-build . build/html
    $ start "" .build\html\index.html

===================
Sphinx Multiversion
=================== 

Builds are versioned by branch/tag, and each version is built in its own directory. This allows you to host multiple versions of 
your documentation on the same server.

.. code-block:: bash

    $ pip install sphinx sphinx-multiversion
    $ sphinx-multiversion source build/html # build directory per branch in build/html where branch = directory name
    $ sphinx-build . build/html -c source -D master_doc=source/index

====
TODO
====

https://jupyterbook.org/en/stable/intro.html
Contact Us
Ask and Answer Questions
Vote for new feagtures ?????  -- use sphinxcontrib.datatemplates to save github repo issues into a datatable
Multi version feature

https://github.com/settings/tokens
