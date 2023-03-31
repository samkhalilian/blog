Docs
====

This blog is written using `ABlog <https://ablog.readthedocs.io>`_ an extension to `Sphinx <https://www.sphinx-doc.orgl>`_
which uses Mark Up language `Restructured Text <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`+.

======
Sphinx
======
Restructerd Text
----------------

=====
ABlog
=====

https://ablog.readthedocs.io/manual/ablog-commands/

.. code-block:: bash

    start       start a new blog project
    build       build your blog project
    clean       clean your blog build files
    serve       serve and view your project
    post        create a blank post
    deploy      deploy your website build files

    See 'ablog <command> -h' for more information on a specific command.

    >> ablog clean && ablog build && ablog serve  # CTRL + C so stop local host
    >> ablog serve -r # to watch yourself blog

Theme
-----

https://github.com/introt/alabester

Comments
--------

.. todo::

    Add comments using Disque https://ablog.readthedocs.io/en/stable/manual/ablog-configuration-options.html#disqus-integration

============
GitHub Pages
============

1. On GitHub create a repo <username>.github.io
2. Make the repo public
3. Then in the command prompt:

.. code-block:: bash

    >> cd Z:/
    >> set GITHUB_USERNAME=samkhalilian
    >> git clone https://github.com/%GITHUB_USERNAME%/%GITHUB_USERNAME%.github.io.git
    >> set REPODIR=Z:/%GITHUB_USERNAME%.github.io
    >> set GITHUB_BRANCH=main
    >> ablog deploy -p %REPODIR% -g %GITHUB_USERNAME% --github-branch %GITHUB_BRANCH% --github-ssh

Windows Bug fix
---------------

line 435: command line is too long fix
Z:\blog\.venv_39\Lib\site-packages\ablog\commands.py

Custom Domain
-------------

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

=============
Google Domain
=============

=====================
Google Cloud Platform
=====================



