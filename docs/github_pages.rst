GitHub Pages
============

These HTML pages are hosted on https://pages.github.com at www.samkhalilian.github.io.

GitHub Pages can be used host a static website for free.

.. warning::

    If your repository is public, GitHub Pages is free.
    If your repository is private, you need a GitHub Pro or GitHub Team plan to use GitHub Pages.

===========
Quick Start
===========

https://docs.github.com/en/pages/quickstart

===============
Diasable Jekyll
===============

GitHub Pages natively suppports `Jekyll <https://jekyllrb.com/>`_, a static site generator, which is used to build a website 
HTML pages from `MarkDown <https://www.markdownguide.org/>`_ source files.

Jekyll is NOT required if you are uploading pre-built HTML files to GitHub Pages i.e. from Sphinx. 

.. important::
    It is possible to bypass Jekyll processing on GitHub Pages by creating a file named .nojekyll in the root of your pages 
    repo and pushing it to GitHub.

======
Deploy
======

These docs are hosted as a static website on https://pages.github.com/.

To deploy the HTML page to GitHub:

.. code-block::

    >> cd Z:\blog\src
    >> set GITHUB_PAGES=samkhalilian
    >> set GITHUB_TOKEN=GITHUB_TOKEN_SAMKHALILIAN_SAMKHALILIAN_GITHUB_IO # environment variable
    >> # set WEBSITE=Z:/blog/src/_website
    >> set REPODIR=Z:/samkhalilian.github.io
    >> set GITHUB_BRANCH=main
    >> # ablog deploy -p %REPODIR% -g %GITHUB_PAGES% --github-token %GITHUB_TOKEN%
    >> ablog deploy -p %REPODIR% -g %GITHUB_PAGES% --github-branch %GITHUB_BRANCH% --github-ssh  # this works

===============
Windows Bug fix
===============

line 435: command line is too long fix
Z:\blog\.venv_39\Lib\site-packages\ablog\commands.py

