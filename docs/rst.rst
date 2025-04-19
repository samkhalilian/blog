reStructuredText
================

These docs are written in mark-up language reStructuredText.

.. seealso::

   https://docutils.sourceforge.io/rst.html
   https://sphinx-tutorial.readthedocs.io/cheatsheet/#rst-cheat-sheet

========
Headings
========

RST lets you define your own section syntax structure.  In these docs we use:

.. code-block:: RST

   Section
   =======
   
   ===========
   Sub Section
   ===========

   Sub Sub Section
   ---------------

   -------------------
   Sub Sub Sub Section
   -------------------

   Sub Sub Sub Sub Section
   ***********************

   ***************************
   Sub Sub Sub Sub Sub Section
   ***************************

=========
Footnotes
=========

.. code-block:: RST

   Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

   .. rubric:: Footnotes

   .. [#f1] Text of the first footnote.
   .. [#f2] Text of the second footnote.

Turn footnotes into sidenotes.

.. code:: python

    html_theme_options = {"use_sidenotes": True}

Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

======
Rubric
======

If you want a section-like element that doesn’t make up the table of contents, consider rubric. 
Is not actually a section, only looks like a minor section to the readers.

.. code:: RST

   .. rubric:: Some minor title not in table of contents

.. [#f1] {-} Text of the first footnote.
.. [#f2] Text of the second footnote.