.. post:: Mar 08, 2024
   :category: Code
   :author: Sam Khalilian

32 vs 64 bit
============

What is the difference between a 32bit and a 64bit program?

The amount of memory available:

* A 32 bit program can use up to 4 gigabytes of memory. 
* A 64 bit program can use up to 18 exabytes\ [*]_ of memory.

So, as long as your program needs to use less than 4GB of memory, there's no real difference.  
But if you need more than that, you need a 64 bit program.

====
Math
====

Where :math:`n` is the number of bits:

.. math::

    (1 \underset{n}{\cdots} 1) = \sum_{i=0}^{n-1} 1 × 2^{i} 

Gives:

* 32 bit binary 11111111111111111111111111111111 converts to 4,294,967,295 (10 digits).
* 64 bit binary 1111111111111111111111111111111111111111111111111111111111111111 converts to 18,446,744,073,709,551,615 (20 digits).

===========
Useful Link
===========

* Binary to integer converter https://www.rapidtables.com/convert/number/binary-to-decimal.html
* Bytes https://en.wikipedia.org/wiki/Orders_of_magnitude_(data)

.. [*] 1 exabyte is 1e9 gigabytes
