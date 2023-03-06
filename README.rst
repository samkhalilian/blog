Blog
====

Create repository in GitHub and then from the command line:

.. code-block:: bash

    >> git init
    >> git add .
    >> git commit -m "first commit"
    >> git branch -M main
    >> git remote add origin https://github.com/samkhalilian/blog.git
    >> git push -u origin main

Dependencies:

.. code-block:: bash

    >> pip install ablog # install https://ablog.readthedocs.io/
    >> pip install Pallets-Sphinx-Themes # install theme
