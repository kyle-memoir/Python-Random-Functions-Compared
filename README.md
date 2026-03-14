# Python Random Functions Compared
Four Python random generation functions compared (one-bit result).

In the course of doing some other work, I had occasion to compare four methods of 
generating a random bit in Python from a performance perspective (no analysis
here on the strength of the generators other than as noted in the comments as per
the Python documentation).

The code is self-explanatory.

On the development platform, Python's random module (test item 1) was fastest on 
large sample sizes and optimized nicely with Numba (70-90% speed boost); the more 
secure os.urandom-based functions (2-4) are not Numba-supported.

Brand new to Python and github -- still tons to learn -- be kind.
