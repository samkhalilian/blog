GitHub
======

In GitHub when creating a new repo its good practice:

* Make it private
* Require a pull request to be created before code can be merged to main
* Require approvals of pull requests

The clone the repo:

.. code-block:: bash

    >> cd Z:/
    >> git clone <https://github.com/<username>/<repo>.git

To create a new repository in GitHub and then from the command line:

.. code-block:: bash

    >> git init
    >> git add .
    >> git commit -m "first commit"
    >> git branch -M main
    >> git remote add origin https://github.com/samkhalilian/blog.git
    >> git push -u origin main

To commit changes to this repo:

.. code-block:: bash

    >> git checkout -b feature/<feature>
    >> # make same changes
    >> git add .
    >> git commit -m "<comment>"
    >> git push --set-upstream origin feature/<feature>

In GitHub approve and merge pull requests.

https://docs.github.com/en/pages/quickstart
