Coding Standards & Best Practices for VBA
=========================================

.. contents::
   :local:
   :depth: 1

==========
Data Types
==========

Overview
--------

- Always explicitly declare variable types.
- Using specific data types improves **performance**, reduces **memory usage**, and prevents **type mismatch errors**.
- Avoid using `Variant` unless absolutely necessary (it's the default if no type is specified).

Common Data Types
-----------------

Best Practices
--------------

- **Use the smallest type that fits the data**.
  - Use `Long` instead of `Integer` for most integer values in modern VBA (internally, VBA converts `Integer` to `Long` anyway).
- **Use `String` instead of `Variant` for text**, unless the variable might be `Null` or multiple types.
- Declare object variables precisely when using early binding:
  - `Dim ws As Worksheet` instead of `Dim ws As Object`

Constants
---------

- When declaring constants, always specify the type:

  .. code-block:: VBScript

     Const PI As Double = 3.14159265
     Const APP_NAME As String = "My VBA Tool"

Arrays
------

- Declare array bounds explicitly:

  .. code-block:: VBScript

     Dim scores(1 To 5) As Integer

- Use dynamic arrays with `ReDim` when needed:

  .. code-block:: VBScript

     Dim data() As Double
     ReDim data(1 To 10)

==================
Naming Conventions
==================

- Use clear, consistent, and descriptive names.

  **Variables**
  - Use camelCase or PascalCase.
  - Optionally prefix with type: `strName`, `intCounter`, `rngData`, `wsSheet`.

  **Procedures**
  - Use verb-based names: `ExportReport()`, `GetUserName()`.

  **Constants**
  - Use all caps with underscores: `PI_VALUE`, `MAX_ATTEMPTS`.

  **Objects**
  - Use meaningful names: `wbReport`, `wsData`, `rngOutput`.

========
Comments
========

- Add header comments for each module, sub, or function.

  Example:

  .. code-block:: VB.net

     '--------------------------------------------------
     ' Sub:    GenerateMonthlyReport
     ' Purpose: Automates the generation of the monthly report
     ' Inputs:  None
     ' Output:  Saves report to a predefined location
     '--------------------------------------------------

- Use inline comments sparingly and only for complex logic.

==============
Error Handling
==============

- Use `On Error GoTo` and handle errors cleanly.

  Example:

  .. code-block:: VB.net

     Sub Example()
         On Error GoTo ErrorHandler

         ' Your code here

         Exit Sub

     ErrorHandler:
         MsgBox "An error occurred: " & Err.Description
     End Sub

===================
Avoid Magic Numbers
===================

- Define constants at the top of your modules.

  .. code-block:: VB.net

     Const MAX_RETRIES As Integer = 3

================
Option Statement
================

Option Explicit
---------------

- Always use `Option Explicit` at the top of every module.
- It forces variable declaration, helping to catch typos and logic errors.
- Without it, VBA will implicitly declare undeclared variables, which can lead to hard-to-debug issues.

  Example:

  .. code-block:: VB.net

     Option Explicit

     Sub Example()
         Dim count As Integer
         count = 10
         MsgBox count
     End Sub

- You can set this as default in the VBA Editor:
  - Go to *Tools > Options > Editor* tab.
  - Check **Require Variable Declaration**.

Option Base
-----------

- `Option Base` controls the default lower bound of **arrays declared without an explicit lower bound**.
- If not specified, **Option Base 0** is assumed (i.e., arrays start from index 0).
- You can specify `Option Base 1` if you want arrays to default from 1 instead.

  Example:

  .. code-block:: VBScript

     Option Base 1

     Sub Example()
         Dim numbers(5) As Integer
         numbers(1) = 10 ' Valid
         numbers(0) = 5  ' Causes error with Option Base 1
     End Sub

- **Best Practice**: Avoid relying on `Option Base`. Instead, always declare array bounds explicitly using `Dim arr(1 To 5)` to avoid confusion and improve clarity.

  .. code-block:: VBScript

     ' Better than relying on Option Base:
     Dim arr(1 To 5) As Integer

- If you do use `Option Base`, be consistent across all modules.

=============================
Early Binding vs Late Binding
=============================

When using external libraries (e.g., Word, Outlook, FileSystemObject), you can bind to them in two ways:

Early Binding
-------------

- **References** are added via *Tools > References* in the VBA editor.
- You declare objects with their specific types (e.g., `Outlook.Application`, `FileSystemObject`).
- Offers **IntelliSense**, compile-time checking, and better performance.
- Requires all users to have the same library versions referenced.

  Example:

  .. code-block:: VBScript

     ' Requires Microsoft Outlook XX.X Object Library reference
     Dim olApp As Outlook.Application
     Set olApp = New Outlook.Application

Late Binding
------------

- You declare objects as `Object` and create them at runtime using `CreateObject`.
- No need to set a reference — more portable and version-independent.
- No IntelliSense and no compile-time checking.

  Example:

  .. code-block:: VBScript

     Dim olApp As Object
     Set olApp = CreateObject("Outlook.Application")

Best Practice
-------------

- **Use Early Binding** during development for IntelliSense and debugging.
- **Switch to Late Binding** for final production code to avoid compatibility issues between different versions of Office or Windows.

--------------
Conversion Tip
--------------

- After development and testing, you can:
  - Remove the reference from Tools > References.
  - Change specific types to `Object`.
  - Replace `New` with `CreateObject`.

===================
Directory Structure
===================

Modularize Code
---------------

- Keep each procedure focused on a single task.
- Break long procedures into smaller reusable ones.

File and Module Organization
----------------------------

- Use clear and consistent module names like: `modUtilities`, `modReporting`, `modMain`.
- Separate business logic, UI, and helper functions.

Code Structure and Readability
------------------------------

- Indent consistently (2–4 spaces).
- Use blank lines between logical sections.
- Group related procedures into the same module.

=====
Tests
=====

- Write test procedures to validate logic.

=======
Logging
=======

- Use `Debug.Print` for output to the Immediate window.

========================
Performance Optimization
========================

- Disable screen updating and automatic calculations during heavy tasks.

  .. code-block:: VB.net

     Application.ScreenUpdating = False
     Application.Calculation = xlCalculationManual

- Use arrays or batch operations instead of cell-by-cell loops.
- Always release object references: `Set ws = Nothing`.

=====================
Avoid Common Pitfalls
=====================

- Avoid `GoTo` (except in error handling).
- Avoid `Select` and `Activate`.

  Bad:

  .. code-block:: VB.net

     Sheets("Data").Select
     Range("A1").Select
     Selection.Value = "Hello"

  Good:

  .. code-block:: VB.net

     Sheets("Data").Range("A1").Value = "Hello"

- Minimize global variables.
