Test Driven Development
=======================

Test driven development (TDD) is a software development process that relies on the repetition of a very short development cycle: 
first the developer writes an (initially failing) automated test case that defines a desired improvement or new function, 
then produces the minimum amount of code to pass that test, and finally refactors the new code to acceptable standards. 
Kent Beck, who is credited with having developed or 'rediscovered' the technique, stated in 2003 that TDD encourages simple 
designs and inspires confidence.

Different types of tests are used in software development, including smoke, unit, regression, user acceptance and performance tests. 
Each type of test serves a different purpose and is used at different stages of the development process.

.. graphviz::

    digraph {
        rankdir=LR;
        node [shape="box"];
        "Unit Test" -> "Integration Test" -> "Smoke Test" -> "Regression Test" -> "User Acceptance Test" -> "Performance Test"
    }

=========
Unit Test
=========

Unit tests are automated tests that are designed to validate the smallest piece of code in an application. They are written
and maintained by developers to ensure that individual units of source code are working as expected. Unit tests are typically
written using a testing framework, such as JUnit, NUnit, or MSTest, and are run automatically as part of the build process.

Example
-------

Example unit test using Python UnitTest:

.. code-block:: python

    import unittest

    def add(x, y):
        return x + y

    class TestAdd(unittest.TestCase):
        def test_addition(self):
            self.assertEqual(add(1, 1), 2)

    if __name__ == '__main__':
        unittest.main()

Coverage
--------

Unit test coverage is a measure used to describe the degree to which the source code of a program is executed when a particular
test suite runs. It is an important metric for software quality and is used to identify areas of code that are not being tested.

You can use the coverage.py tool to measure code coverage in Python programs. To install coverage.py, run the following command:

.. code-block:: bash

    pip install coverage

To run coverage.py on a Python program, use the following command:

.. code-block:: bash

    coverage run my_program.py

To generate a coverage report, use the following command:

.. code-block:: bash

    coverage report

To generate an HTML coverage report, use the following command:

.. code-block:: bash

    coverage html

The HTML coverage report will be saved in the htmlcov directory.

================
Integration Test
================

Integration tests are used to verify that different components of an application work together correctly. They are designed
to test the interactions between different modules or services and are used to validate that the system as a whole behaves as
expected. Integration tests are typically more complex than unit tests and may involve multiple components or services.

==========
Smoke Test
==========

A smoke test is a preliminary to further testing, which is used to verify that the basic functionalities of a component are
working correctly. Smoke tests are a subset of test cases that cover the most important functionality of a component or system,
used to verify that the most crucial functions of a program work, but not bothering with finer details. Smoke tests are
usually scripted by developers and are run by testers before accepting a build for further testing.


===============
Regression Test
===============

Regression tests are used to verify that a recent code change has not adversely affected the existing functionality of an
application. They are typically run after a new feature has been added or a bug has been fixed to ensure that the change has
not introduced any new defects. Regression tests are usually automated and are run as part of the continuous integration
process.

====================
User Acceptance Test
====================

User acceptance tests (UAT) are used to verify that an application meets the requirements of the end user. They are typically
written by business analysts or product owners and are used to validate that the application behaves as expected from the
user's perspective. UATs are usually run manually by testers or end users and are used to determine whether the application
is ready for release.

================
Performance Test
================

Performance tests are used to verify that an application meets the performance requirements of the end user. They are used to
measure the speed, responsiveness, and stability of an application under various load conditions. Performance tests are
typically run by performance engineers and are used to identify bottlenecks and optimize the performance of an application.
