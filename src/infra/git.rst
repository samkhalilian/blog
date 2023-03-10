.. post:: Oct 12, 2022
   :category: Programming
   :tags: Infra
   :author: Sam Khalilian

Git
===

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

    >> git add .
    >> git commit -m "..."
    >> git push
