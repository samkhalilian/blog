Learn to Code Documentation
===========================

=====
About
=====

Welcome to my quantitative development notes!

These pages provide learning resources on math, coding, and trading. They are based on the author's experience in academia and industry. 

.. seealso::
    
    You can find more details about me at `LinkedIn <https://www.linkedin.com/in/sam-khalilian-453704146>`_.

===========
Quick Start
===========

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
    $ sphinx-build -M html source build
    $ start "" build\html\index.html
