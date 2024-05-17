## Problem Overview
This is a Python program that implements the so-called "Russian Peasant" or "Ancient Egyptian" multiplication algorithm.  This algorithm is an alternative to the multiplication process taught in elementary school. To learn more information on why the algorithm works, please see [this wikipedia page](http://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication) or [other sites](http://www.cut-the-knot.org/Curriculum/Algebra/PeasantMultiplication.shtml).

Here is how the algorithm works. Suppose you wish to multiply two integers ``A`` and ``B`` together (no decimals allowed). 

* You would first write the values of ``A`` and ``B`` side-by-side in two columns.
* Then you create a new row with twice the previous value in the ``A`` column, and half the previous value (truncated) in the ``B`` column.
*  Continue this doubling/halving step until the value in the ``B`` column is zero.
*  Finally, add up all of the values in the ``A`` column that go with an odd value in the ``B`` column.  That sum will be the product of the original ``A`` and ``B`` values.

DONE WITH C++