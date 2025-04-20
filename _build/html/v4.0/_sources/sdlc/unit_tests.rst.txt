Unit Tests
==========

Unit tests are a critical part of the software development process. They help ensure that individual components of the 
software work as expected. In this section, we will discuss how to write and run unit tests for the code in this repository.

=================
Python Unit Tests
=================

unittest
--------

.. seealso::
    
    `unittest documentation <https://docs.python.org/3/library/unittest.html>`_

Python has a built-in module called `unittest` that provides a framework for writing and running unit tests.
It is a powerful tool that allows you to create test cases, group them into test suites, and run them with a test runner.

.. code-block:: python

    import unittest

    class TestMathOperations(unittest.TestCase):
        def test_addition(self):
            self.assertEqual(1 + 1, 2)

        def test_subtraction(self):
            self.assertEqual(2 - 1, 1)

    if __name__ == '__main__':
        unittest.main()

pytest
------

.. seealso::

    `pytest documentation <https://docs.pytest.org/en/stable/>`_

Alternatively, you can use `pytest`, a third-party testing framework that is more flexible and easier to use than `unittest`.
It allows you to write simple test functions and provides powerful features like fixtures, parameterized tests, and plugins.

.. code-block:: python

    import pytest

    def test_addition():
        assert 1 + 1 == 2

    def test_subtraction():
        assert 2 - 1 == 1

    if __name__ == '__main__':
        pytest.main()

unittest vs pytest
------------------

Both `unittest` and `pytest` have their pros and cons. `unittest` is part of the standard library, so it doesn't require any 
additional installation. However, it can be more verbose and less flexible than `pytest`. On the other hand, `pytest` is more 
user-friendly and has a rich ecosystem of plugins, but it requires an additional installation step.

.. csv-table:: Comparison of unittest and pytest
    :header: "Feature", "unittest", "pytest"
    :widths: 20, 20, 20

    "Installation", "Built-in", "Requires install"
    "Syntax", "Verbose", "Concise"
    "Test Discovery", "Manual", "Automatic"
    "Fixtures", "Limited", "Extensive"
    "Plugins", "None", "Rich ecosystem"

==============
C++ Unit Tests
==============