.. post:: Oct 12, 2022
   :category: Programming
   :tags: Python

Args & Kwargs
=============

*args and **kwargs allow you to pass an undefined number of arguments and keywords when calling a function.

https://github.com/wilfredinni/python-cheatsheet/blob/master/docs/cheatsheet/args-and-kwargs.md

.. code-block:: python

   def foo(*args):
      ...

   >> x = [1, 2, 3, 4, 5]
   >> foo(x)
   >> foo(1, 2, 3, 4)


.. code-block:: python

   def foo(**kwargs):
      ...

   >> x = {"a": 1, "b": 2, "c": 3}
   >> foo(x)
  
  
