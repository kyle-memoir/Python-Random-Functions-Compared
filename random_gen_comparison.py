# Random Generator Comparison - Python
# source code by Kyle Memoir

"""
Elapsed time given in microseconds (μs).

Time includes interpreter overhead; use a large sample size for 
best results (n = 1000000 is a reasonable minimum starting point). 

Times will vary stochastically as system load varies.

Set n = 1 to expose interpreter overhead for each method.

The results 'bit' is a sample generated in the print statement after 
measurement.

"""

import random
import secrets
import time
import os


# Set sample size (no commas)
n = 1000000

print(f"\nRandom Generator Comparison (n = {n:,})\
\n\n     t/iteration (μs)  bit   source")

# 1. random.randint - pseudorandom (Mersenne twister/software seeded)
#    see: https://docs.python.org/3/library/random.html#module-random
start_rnd = time.time()
for _ in range(n):
    random.randint(0, 1)
# microseconds (μs) per call
print(f"\n1.  {((time.time() - start_rnd) / n * 1000000):.15f}s ({random.randint(0, 1)}) random.randint")


# 2. os.urandom - strong (hardware-dependent entropy source)
#    see: https://docs.python.org/3/library/os.html
start_osu = time.time()
for _ in range(n):
    (os.urandom(1))[0] & 1
# microseconds (μs) per call
print(f"2.  {((time.time() - start_osu) / n * 1000000):.15f}s ({(os.urandom(1))[0] & 1}) os.urandom")


# 3. random.SystemRandom - strong (function built on os.random)
#    see: https://docs.python.org/3/library/random.html#random.SystemRandom
start_rsr = time.time()
sec_gen = random.SystemRandom()
for _ in range(n):
    sec_gen.randint(0, 1)
# microseconds (μs) per call
print(f"3.  {((time.time() - start_rsr) / n * 1000000):.15f}s ({sec_gen.randint(0, 1)}) random.SystemRandom (os.urandom)")


# 4. secrets.randbits - strong (function built on os.random)
#    see: https://docs.python.org/3/library/secrets.html
start_sec = time.time()
for _ in range(n):
    secrets.randbits(1)
# microseconds (μs) per call
print(f"4.  {((time.time() - start_sec) / n * 1000000):.15f}s ({secrets.randbits(1)}) secrets.rndbits (os.urandom)\n")
