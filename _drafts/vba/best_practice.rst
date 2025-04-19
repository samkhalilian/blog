.. post:: Feb 07, 2025
   :category: Code
   :tags: VBA
   :author: Sam Khalilian
  
Best Practices for VBA
======================

Microsoft Excel is still a tool widely used in Finance and Trading for analysis and reporting.

Developement of Excel using Visual Basic for Applications (VBA) can be challenging due to the lack of modern development tools and practices.   

Here we provide some best practices for developing Excel VBA applications.

.. .. contents:: Table of Contents
   :depth: 1
   :local:

==================
Naming Conventions
==================

Use camelCase for variables and PascalCase for functions, procedures and classes.

Prefix variables with the data type e.g. strName, intCount, rngData.

.. code-block:: vbnet

    Dim strName As String
    Dim intCount As Integer
    Dim rngData As Range

Classes should be prefixed with cls e.g. clsPerson, clsTrade.

Forms should be prefixed with frm e.g. frmMain, frmSettings.

Dont use Variant data type unless necessary.  Explicit is better than implicit.

Use meaningful names for variables, functions and procedures.

.. code-block:: vbnet

    Dim strReportName As Integer

    Sub CreateReport()
        ' code here
    End Sub

===============
Option Explicit
===============

Option Explicit is a statement that forces the declaration of all variables in a module.  
This is a good practice to avoid errors due to undeclared variables.

.. code-block:: vbnet

    Option Explicit

    Dim strName As String # variable declaration

==============
Error Handling
==============

Use error handling to catch out of bounds errors.

Use On Error Resume Next to continue execution after an error.

Use On Error GoTo 0 to stop error handling.

Use Err.Number to get the error number.

Use Err.Description to get the error description.

.. code-block:: vbnet

    On Error Resume Next
    ' code here
    If Err.Number <> 0 Then
        MsgBox Err.Description
    End If
    On Error GoTo 0

=====================
Early vs Late Binding
=====================

Early binding is when the object library is referenced at compile time.

Late binding is when the object library is referenced at runtime.

Early binding is faster and provides intellisense, but requires the object library to be available on the machine.

E.g. Early binding to the Excel object library or Dictionary object.

E.g. Late binding to the Excel object library or Dictionary object.

.. code-block:: vbnet
    
    ' Early binding to Excel object library
    Dim xlApp As Excel.Application
    Set xlApp = New Excel.Application

    ' Late binding to Excel object library
    Dim xlApp As Object
    Set xlApp = CreateObject("Excel.Application")

======
Bounds
======

Use the LBound and UBound functions to get the lower and upper bounds of an array.

.. code-block:: vbnet

    Dim arrData(1 To 10) As Integer
    Dim i As Integer
    For i = LBound(arrData) To UBound(arrData)
        Debug.Print arrData(i)
    Next i

==========
Navigation
==========

Use xlright, xlDown, xlUp, xlToLeft to navigate a range.

.. code-block:: vbnet

    Dim rngData As Range
    Set rngData = Range("A1:A10")
    Debug.Print rngData.End(xlDown).Row

==========
The Ribbon
==========

The Ribbon is the toolbar at the top of the Excel application and can be customised using XML which is embedded in the Excel file.

To access the XML:

1. Rename the file (.xlxx/.xlsm/.xlsb) extension to .zip.
2. Unzip the file.
3. Open the customUI folder.
4. The XML is stored in the customUI14.xml file.
5. Make changes to the XML and save the file.
6. Rename the file  back to its original file extension.

Example of customisig the XML:

.. code-block:: xml

    <mso:customUI xmlns:mso='http://schemas.microsoft.com/office/2009/07/customui'>
    <mso:ribbon>
    <mso:qat>
    <mso:sharedControls>
    <mso:control idQ='mso:PrintPreviewAndPrint' visible='true'/>
    </mso:sharedControls>
    </mso:qat>
    </mso:ribbon>
    </mso:customUI>

The Ribbon can also be customised using VBA:

.. code-block:: vbnet

    Sub AddRibbon()
        Dim ribbonXML As String
        ribbonXML = "<mso:customUI xmlns:mso='http://schemas.microsoft.com/office/2009/07/customui'>"
        ribbonXML = ribbonXML & "<mso:ribbon>"
        ribbonXML = ribbonXML & "<mso:qat>"
        ribbonXML = ribbonXML & "<mso:sharedControls>"
        ribbonXML = ribbonXML & "<mso:control idQ='mso:PrintPreviewAndPrint' visible='true'/>"
        ribbonXML = ribbonXML & "</mso:sharedControls>"
        ribbonXML = ribbonXML & "</mso:qat>"
        ribbonXML = ribbonXML & "</mso:ribbon>"
        ribbonXML = ribbonXML & "</mso:customUI>"
        Application.CustomUIs.Add ribbonXML
    End Sub
