==============
Data Templates
==============

.. code-block:: bash

    $ pip install sphinxcontrib-datatemplates

.. .. datatemplate:: github_issues
    :github_repo: samkhalilian/blog
    :github_token: %GITHUB_TOKEN%

.. code-block:: python

    # conf.py
    extensions = [
        'sphinxcontrib.datatemplates',
    ]

    datatemplates_github_issues = {
        'github_repo': 'samkhalilian/blog',
        'github

.. code-block:: python

    def fetch_github_issues(repo, token):
        import requests
        url = f'https://api.github.com/repos/{repo}/issues'
        headers = {'Authorization': f'token {token}'}
        response = requests.get(url, headers=headers)
        return response.json()

.. code-block:: rst

    .. datatemplate:: github_issues
        :github_repo: samkhalilian/blog
        :github_token: %GITHUB_TOKEN%