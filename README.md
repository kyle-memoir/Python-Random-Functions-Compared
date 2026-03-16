# Python Random Functions Compared
Four Python random generation functions compared (one-bit result).

In the course of doing some other work, I had occasion to compare four methods of 
generating a random bit in Python from a performance perspective (no analysis
here on the strength of the generators other than as noted in the comments as per
the Python documentation).

The code is self-explanatory.

On the development platform, Python's 'random' module (test item 1) was fastest on 
large sample sizes and optimized nicely with Numba (70-90% speed boost); the more 
secure os.urandom-based functions (2-4) are not Numba-supported. Numba testing is
not included in this analysis, nor any other such performance enhancement approach
such as using Cython, Rust or multiprocessing.

Test items 1(a) and 1(b) illustrate there can be meaningful performance differences
using differing methods of the same function to generate the same desired outcome.

Brand new to Python and github -- still tons to learn -- be kind.
