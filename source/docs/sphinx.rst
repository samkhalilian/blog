Sphinx
======

.. contents::
   :local:
   :depth: 1

These docs have been published using Sphinx. 

.. seealso::

   .. line-block::
   
      https://www.sphinx-doc.org
      https://sphinx-tutorial.readthedocs.io/cheatsheet/#sphinx-cheat-sheet

=======
Install
=======

Install a recent version of Python from https://www.python.org/downloads/.

Create and activate a :doc:`Virtual Environment <../python/venv>` and install Sphinx.

.. code::

   $ pip install Sphinx

===========
Quick Start
===========

Use Sphinx quick start to setup directories and basic configuration for a new project.

.. code::

   $ sphinx-quickstart --sep

.. note::

    Option :code:`--sep` will create separate source and build directories.

.. code::

   project
   ├── .venv
   ├── build
   |── source
   |   ├── conf.py
   |   └── index.rst
   └── requirements.txt

Where

* *build* directory stores the generated HTML pages
* *source* directory stores :doc:`reStructuredText <rst>` files used to edit the contents of HTML pages
* *conf.py* is used to configure the HTML pages e.g. theme, extensions etc

.. code-block:: python
   :caption: source/conf.py
   
   project = "Learn to Code"
   copyright = '2024, Sam Khalilian'
   author = 'Sam Khalilian'
   release = '0.0.1'
   html_title = "Learn to Code"
   html_theme = "pydata_sphinx_theme"
   extensions = []
   
* *index.rst* is the landing page

.. code-block:: rst
   :caption: source/index.rst
      
   Learn to Code Documentation
   ===========================

   ...

=====
Build
=====

To build and open the docs

.. code:: bash

   $ sphinx-build -M html source build
   $ start "" build\html\index.html

======
Themes
======

A Sphinx theme helps shape your documentation’s appearance and usability.  Sphinx provides a number of 
`themes <https://www.sphinx-doc.org/en/master/usage/theming.html>`_.  In these docs, we use the 
`PyData <https://pydata-sphinx-theme.readthedocs.io/en/stable/>`_ theme.

Install

.. code:: bash

   $ pip install pydata-sphinx-theme

Set config.py

.. code:: python

   html_theme = "pydata_sphinx_theme"

=====
ABlog
=====

We use `ABlog <https://ablog.readthedocs.io>`_ a Sphinx extension that offers blog style features to tag pages 
as blog posts.

Install ABlog

.. code::

   $ pip install ablog

To tag a page as a blog post add the following to the top of a page

.. code:: rst

   .. post:: <DATE>
      :category: <CATEGORY>
      :tag: <TAG>
      :author: <AUTHOR>

E.g. 

.. code-block:: rst
   :caption: source/release/release_1_0_0.rst
   
   .. post:: Mar 28, 2023
      :category: Release
      :tags: Release
      :author: Sam Khalilian

=============
Multi-Version
=============

.. code-block:: bash

   $ pip install sphinx-multiversion



========
Comments
========

Disque

pip install sphinxcontrib-disqus

xtensions.append("sphinxcontrib.disqus")

# Set your Disqus shortname (replace with your Disqus site's shortname)
.. disqus_shortname = "your-disqus-shortname"

.. .. disqus::




Utterances (GitHub Comments on Each Page)

.. include:: sphinx_pygments.rst

.. .. include:: sphinx_plot.rst

.. .. include:: sphinx_extensions.rst

.. include:: sphinx_design.rst

.. include:: sphinx_file.rst

.. include:: sphinx_data_templates.rst


Extensions
==========