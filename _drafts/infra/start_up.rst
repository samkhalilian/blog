Start Up
========

A start up file is useful to set the working environment. On Windows 11 press WIN+R and run:

.. code-block:: bash

    $ shell::startup

Which opens the start up directory

`<file:///%APPDATA%/Microsoft/Windows/Start%20Menu/Programs/Startup>`_

Any file you save in 

Then create a new file in this directory

.. code-block:: bat

    $ CD %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
    $ ECHO > start_up.cmd

In the start up file we can:

* Map drives
* Load apps
* ...

In particular we map this projects working directy to Z: and launch :doc:`Windows Terminal <windows_terminal>`.

.. code-block:: bat
    :linenos:
    
    REM start_up.cmd

    REM map drives
    SUBST Z: /D
    SUBST Z: C:\Users\samkh\OneDrive\project
        
    REM load shell
    START Z:\cli.cmd

    EXIT
