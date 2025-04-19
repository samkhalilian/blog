Release Notes
=============

========================
Generating Release Notes
========================

GitHub provides functionality to automatically generate release notes:

* https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes
* https://dev.to/github/how-to-automatically-generate-release-notes-for-your-project-2ng8

==================
Release vs Version
==================

https://stackoverflow.com/questions/20184055/what-if-any-is-the-difference-between-a-software-release-and-a-version

----------------------
https://stackoverflow.com/questions/51884336/snapshot-version-vs-release-version
There is a method called semantic versioning. Your version numbers look like X.Y.Z.

Increment X if there is a change breaking backwards compatibility
Increment Y for new features
Increment Z for bugfixes
----------------------

-----------------------
https://py-pkgs.org/07-releasing-versioning.html

Patch release (0.1.0 -> 0.1.1): patch releases are typically used for bug fixes, which are backward compatible. Backward compatibility refers to the compatibility of your package with previous versions of itself. For example, if a user was using v0.1.0 of your package, they should be able to upgrade to v0.1.1 and have any code they previously wrote still work. It’s fine to have so many patch releases that you need to use two digits (e.g., 0.1.27).

Minor release (0.1.0 -> 0.2.0): a minor release typically includes larger bug fixes or new features that are backward compatible, for example, the addition of a new function. It’s fine to have so many minor releases that you need to use two digits (e.g., 0.13.0).

Major release (0.1.0 -> 1.0.0): release 1.0.0 is typically used for the first stable release of your package. After that, major releases are made for changes that are not backward compatible and may affect many users. Changes that are not backward compatible are called “breaking changes”. For example, changing the name of one of the modules in your package would be a breaking change; if users upgraded to your new package, any code they’d written using the old module name would no longer work, and they would have to change it.
----------------------

--------------------------
https://stackoverflow.com/questions/34336383/what-are-the-standard-python-meanings-of-version-and-release
Sphinx has the notion of a "version" and a "release" for the software. Each version can have multiple releases. 
For example, for Python the version is something like 2.5 or 3.0, while the release is something like 
2.5.1 or 3.0a1. If you don't need this dual structure, just set both to the same value.
--------------------------

What is the difference between the Release and Version of an application?

A public or production (PROD) release is a version for end users who are not involved in testing (UAT) or 
development of the application.

The version makes reference to the release edition and any major or minor changes e.g version 2.1.5 means it's 
the second edition with at least 1 major change from its 2.0 predecessor and 5 minor changes.

In Sphinx release and versions are set in config.py:

.. code:: python

    # The short X.Y version.
    version = "1.0.0"
    # The full version, including alpha/beta/rc tags.
    release = "UAT 1.0.0 20230327"
