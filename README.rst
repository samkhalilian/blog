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
    $ sphinx-build -M html source build # create HTML pages in build\html
    
    $ start "" build\html\index.html # open in browser
    
    $ python -m http.server -d build/html # serve on localhost:8000
    $ start http://localhost:8000/index.html # open in browser
