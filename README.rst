Blog
====

Create repository on command line:

. code-block:: bash

    # >> echo "# blog" >> README.md
    >> git init
    >> git add README.md
    >> git commit -m "first commit"
    >> git branch -M main
    >> git remote add origin https://github.com/samkhalilian/blog.git
    >> git push -u origin main

Dependencies:

. code-block:: bash

    >> pip install ablog # install https://ablog.readthedocs.io/
    >> pip install Pallets-Sphinx-Themes # install theme
