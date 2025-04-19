Continuous Integration
======================

Continuous integration is a software development practice where developers regularly merge their code changes into a central
repository, after which automated builds and tests are run. The goal of continuous integration is to detect and fix integration
errors as quickly as possible, and to ensure that the software is always in a releasable state.

Github Actions is a feature of GitHub that allows you to automate your software development workflows. You can use GitHub
Actions to build, test, and deploy your code right from GitHub. GitHub Actions are event-driven, meaning that they are triggered
by events such as pushes to a repository, pull requests, or issue comments.


GitHub Actions is a feature of GitHub that allows you to automate your software development workflows. You can use GitHub
Actions to build, test, and deploy your code right from GitHub. GitHub Actions are event-driven, meaning that they are triggered
by events such as pushes to a repository, pull requests, or issue comments.

Example GitHub Actions workflow:

.. code-block:: yaml

    name: Python application

    on:
      push:
        branches:
          - master

    jobs:
      build:

        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v2
        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: '3.x'
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
        - name: Run tests
          run: |
            python -m unittest discover tests
        - name: Deploy
          run: |
            echo "Deploying to production"

