.. post:: Oct 14, 2022
   :category: Programming
   :tags: Python
   :author: Sam Khalilian

requirements.txt
================

Manage required Python packages with requirements.txt:

.. code-block:: bash

   >> cd %DIR_PROJECT%
   >> pip freeze > requirements.txt # output list of installed Python packages and versions
   >> pip install -r requirements.txt
   >> python -m pip check # check for missing dependencies

https://stackoverflow.com/questions/29222269/is-there-a-way-to-have-a-conditional-requirements-txt-file-for-my-python-applica
https://stackoverflow.com/questions/11889932/specify-python-version-for-virtualenv-in-requirements-txt
Python version dependencies can be managed
https://stackoverflow.com/questions/19559247/requirements-txt-depending-on-python-version