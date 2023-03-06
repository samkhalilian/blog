.. post:: Oct 12, 2022
   :category: Programming
   :tags: Python

__init__.py
===========

The __init__.py file indicates that the files in a folder are part of a Python package. 
Without an __init__.py file, you cannot import files from another directory in a Python project.

For example

.. code-block:: bash

   dir/sub_dir/__init__.py
   dir/sub_dir/module.py

where

.. code-block:: bash

   # dir/sub_dir/module.py
   def hello():
      print('hello')

and dir is on your path, you can import the code in module.py as:

.. code-block:: bash

   import sub_dir.module
   from sub_dir.module import hello

If you remove the __init__.py file, Python will no longer look for submodules inside that directory, 
so attempts to import the module will fail.

Without it, however, you can't import directly. You have to amend the system path:

.. code-blok:: bash

   import sys
   sys.path.insert(0, 'dir/sub_dir/module.py')

   from module import hello