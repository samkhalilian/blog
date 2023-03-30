Docs
====

======
Sphinx
======

Restructerd Text
----------------

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
    >> set REPODIR=Z:/blog/samkhalilian.github.io
    >> set REPODIR=samkhalilian.github.io
    >> ablog deploy -p %REPODIR% -g %GITHUB_PAGES% --github-token %GITHUB_TOKEN%
    >> ablog deploy -p %REPODIR% -g %GITHUB_PAGES% --github-ssh 

Custom Domain
-------------

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

=============
Google Domain
=============

=====================
Google Cloud Platform
=====================

