Docs
====

======
Sphinx
======

Restructerd Text
----------------

https://spl.hevs.io/spl-docs/writing/rst/cheatsheet.html

=====
ABlog
=====

This blog is written using `ABlog <https://ablog.readthedocs.io>`_ an extension to `Sphinx <https://www.sphinx-doc.orgl>`_
which uses Mark Up language `Restructured Text <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`+.

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

============
GitHub Pages
============

.. code-block:: bash

    >> set GITHUB_PAGES=samkhalilian
    >> set GITHUB_TOKEN=GITHUB_TOKEN_SAMKHALILIAN_SAMKHALILIAN_GITHUB_IO
    >> set WEBSITE=Z:/blog/src/_website
    >> set REPODIR=Z:/samkhalilian.github.io
    >> set GITHUB_BRANCH=main
    >> ablog deploy -p %REPODIR% -g %GITHUB_PAGES% --github-token %GITHUB_TOKEN%
    >> ablog deploy -p %REPODIR% -g %GITHUB_PAGES% --github-branch %GITHUB_BRANCH% --github-ssh  # this works

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

