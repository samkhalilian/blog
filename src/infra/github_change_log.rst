GitHub Change Log
=================

GitHub repo release notes are saved to:

* https://github.com/<username>/<repo>/releases
* https://github.com/<username>/<repo?/releases/tag/<tag>

The release notes can be read by:

https://github.com/ewjoachim/sphinx-github-changelog

.. code:: bash

    >> pip install sphinx-github-changelog

    # conf.py
    extensions = [
        ...,
        "sphinx_github_changelog",
    ]

    # assign a github api token to environment variable
    sphinx_github_changelog_token = os.environ["SPHINX_GITHUB_CHANGELOG_TOKEN"]

    .. changelog::
        :github: https://github.com/<username>/<repo>/releases


.. changelog::
    :changelog-url: ""
    :github: https://github.com/samkhalilian/blog/releases/
