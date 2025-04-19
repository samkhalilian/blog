.. post:: Feb 03, 2025
   :category: Code
   :tags: Shell
   :author: Sam Khalilian

.. update:: 09 Feb, 2025


CMD
=== 

CMD (Command Prompt) is a Windows OS CLI and command language.

It is used to execute entered commands. Most of the commands are used to automate tasks via scripts and batch files, perform 
advanced administrative functions, and troubleshoot and solve certain kinds of Windows issues.

========
Commands
========

A list of useful commands:

.. code-block:: bat

    $ dir # list directory contents
    $ cd <PATH> # change directory
    $ cd .. # move up one directory
    $ mkdir <DIRECTORY> # create directory
    $ del <FILE> # delete file
    $ rmdir <DIRECTORY> # remove directory
    $ copy <SOURCE> <DESTINATION> # copy file
    $ move <SOURCE> <DESTINATION> # move file
    $ type <FILE> # display file contents
    $ echo <TEXT> > <FILE> # write text to file
    $ echo <TEXT> >> <FILE> # append text to file
    $ cls # clear screen
    $ exit # exit command prompt
    $ ipconfig # display IP configuration
    $ ping <HOST> # ping host

    $ tasklist # list running processes
    $ taskkill /F /IM <PROCESS> # kill process
    $ shutdown /s # shutdown computer
    $ shutdown /r # restart computer
    $ shutdown /l # log off user
    $ systeminfo # display system information
    $ hostname # display computer name
    $ net use # display mapped drives
    $ net use <DRIVE>: <PATH> # map network drive
    $ net use <DRIVE>: /delete # disconnect network drive
    