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
   >> python -m pip check # check for missing dependenciesS