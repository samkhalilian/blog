.. post:: Feb 07, 2025
   :category: Code
   :tags: SQL
   :author: Sam Khalilian
 
Best Practices for SQL 
======================

SQL is a standard language for storing, manipulating and retrieving data in relational databases.

It is the foundation for many data analysis tools and is widely used in Finance and Trading for analysis and reporting.

Developement of SQL queries can be challenging due to the complexity of the language and the need to optimize performance.

Here we provide some best practices for developing SQL queries.

.. contents:: Table of Contents
   :depth: 1
   :local:

==================
Naming Conventions
==================

Use snake_case for table, column names and capitals for statement.

.. code-block:: sql

    SELECT 
        column_name 
    FROM table_name 
    WHERE column_name = 'value';

==========
Data Types
==========

Use the correct data type for the column.

.. code-block:: sql

    CREATE TABLE table_name (
        column_name INT,
        column_name TEXT,
        column_name DATE
    );


======
PRAGMA
======

Use PRAGMA to set the schema and optimize the query.

.. code-block:: sql

    PRAGMA foreign_keys = ON;

    PRAGMA journal_mode = WAL;

    PRAGMA synchronous = NORMAL;

    PRAGMA cache_size = 10000;