========
Pygments
========

Pygments is a syntax highlighting engine written in Python. It is used to format code in many programming languages. 
It is used in Sphinx to highlight code blocks in documentation.

.. seealso::

   https://pygments.org

Install
-------

To install Pygments, use pip.

.. code:: bash

   $ pip install Pygments

Lexers
------

Pygments can be used to highlight code in many languages.  Those used in these docs:

.. csv-table:: Pygments Lexers in Sphinx used in these docs
   :header-rows: 1
   :file: sphinx_pygments.csv

A list of all supported languages see https://pygments.org/languages/.

To specify the language of the code block, add the Lexer name after the double colons.

.. code-block:: bash

    .. code-block:: python

        # Python code block
        def hello_world():
            print("Hello, World!")

.. note::

    If a language is not supported by Pygments, the code block will not be highlighted.

    If a language is not specified, the default language is Python.