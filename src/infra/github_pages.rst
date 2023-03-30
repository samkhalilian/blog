GitHub Pages
============

`GitHub Pages <https://pages.github.com/>`_ can be used host a static website for free.

GitHub Pages uses `MarkDown <https://www.markdownguide.org/>`_ which is turned in to HTML by `Jekyll <https://jekyllrb.com/>`_.

.. warning::
    It is possible to bypass Jekyll processing on GitHub Pages by creating a file named .nojekyll in the root of your pages 
    repo and pushing it to GitHub.

    This should only be necessary if your site uses files or directories that start with underscores since Jekyll considers 
    these to be special resources and does not copy them to the final site.
 
For Sphinx docs to render correctly on GitHub Pages: 

.. code:: bash

    >> pip install sphinxtogithub

    # creates .nojekyll file to ignore _static, _sources folders 
    extensions = [
        ...
        'sphinx.ext.githubpages ',
    ]
