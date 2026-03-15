# Random Generator Comparison - Python
# source code by Kyle Memoir

"""
Elapsed time given in microseconds (μs).

Time includes interpreter overhead; use a large sample size for 
best results (n = 1000000 is a reasonable minimum starting point). 

Times will vary stochastically as system load varies.

Series A (n = 1) exposes interpreter overhead for each method.
Series B (n = 1,000,000) exposes function speed.

The results 'bit' is a sample generated after measurement.

"""

import random
import secrets
import time
import os


print("\n\n      Python Random Number Generators")

# A. Sample size 1 (interpreter overhead)

n = 1

print(f"\nSeries A - RNG Load Speed (n = {n:,})\
\n\n     t/iteration (μs)  bit   source")

# 1. random.randint - pseudorandom (Mersenne twister/software seeded)
#    see: https://docs.python.org/3/library/random.html#module-random
start_rnd = time.time()
for _ in range(n):
    random.randint(0, 1)
t = time.time()
run_time = (t - start_rnd)
# microseconds (μs) per call
print(f"1(a).  {run_time / n * 1000000:.15f} ({random.randint(0, 1)}) random.randint")

# 1(b). random.randrange - pseudorandom (Mersenne twister/software seeded)
#    see: https://docs.python.org/3/library/random.html#module-random
start_rnd = time.time()
for _ in range(n):
    random.randrange(0, 2)
t = time.time()
run_time = (t - start_rnd)
# microseconds (μs) per call
print(f"1(b).  {run_time / n * 1000000:.15f} ({random.randrange(0, 1)}) random.randrange")


# 2. os.urandom - strong (hardware-dependent entropy source)
#    see: https://docs.python.org/3/library/os.html
start_osu = time.time()
for _ in range(n):
    os.urandom(1)  #[0] & 1
t = time.time()
run_time = (t - start_osu)
# microseconds (μs) per call
print(f"2.  {run_time / n * 1000000:.15f} ({(os.urandom(1))[0] & 1}) os.urandom")


# 3. random.SystemRandom - strong (function built on os.random)
#    see: https://docs.python.org/3/library/random.html#random.SystemRandom
start_rsr = time.time()
sec_gen = random.SystemRandom()
for _ in range(n):
    sec_gen.randint(0, 1)
t = time.time()
run_time = (t - start_rsr)
# microseconds (μs) per call
print(f"3.  {run_time / n * 1000000:.15f} ({sec_gen.randint(0, 1)}) random.SystemRandom")


# 4. secrets.randbits - strong (function built on os.random)
#    see: https://docs.python.org/3/library/secrets.html
start_sec = time.time()
for _ in range(n):
    secrets.randbits(1)
t = time.time()
run_time = (t - start_sec)
# microseconds (μs) per call
print(f"4.  {run_time / n * 1000000:.15f} ({secrets.randbits(1)}) secrets.randbits")



# B. Sample size 1,000,000 (function speed)

n = 1000000

print(f"\nSeries B - RNG Function Speed (n = {n:,})\
\n\n     t/iteration (μs)  bit   source")

# 1. random.randint - pseudorandom (Mersenne twister/software seeded)
#    see: https://docs.python.org/3/library/random.html#module-random
start_rnd = time.time()
for _ in range(n):
    random.randint(0, 1)
t = time.time()
run_time = (t - start_rnd)
# microseconds (μs) per call
print(f"1(a).  {run_time / n * 1000000:.15f} ({random.randint(0, 1)}) random.randint")

# 1(b). random.randrange - pseudorandom (Mersenne twister/software seeded)
#    see: https://docs.python.org/3/library/random.html#module-random
start_rnd = time.time()
for _ in range(n):
    random.randrange(0, 2)
t = time.time()
run_time = (t - start_rnd)
# microseconds (μs) per call
print(f"1(b).  {run_time / n * 1000000:.15f} ({random.randrange(0, 1)}) random.randrange")


# 2. os.urandom - strong (hardware-dependent entropy source)
#    see: https://docs.python.org/3/library/os.html
start_osu = time.time()
for _ in range(n):
    os.urandom(1)  #[0] & 1
t = time.time()
run_time = (t - start_osu)
# microseconds (μs) per call
print(f"2.  {run_time / n * 1000000:.15f} ({(os.urandom(1))[0] & 1}) os.urandom")


# 3. random.SystemRandom - strong (function built on os.random)
#    see: https://docs.python.org/3/library/random.html#random.SystemRandom
start_rsr = time.time()
sec_gen = random.SystemRandom()
for _ in range(n):
    sec_gen.randint(0, 1)
t = time.time()
run_time = (t - start_rsr)
# microseconds (μs) per call
print(f"3.  {run_time / n * 1000000:.15f} ({sec_gen.randint(0, 1)}) random.SystemRandom")


# 4. secrets.randbits - strong (function built on os.random)
#    see: https://docs.python.org/3/library/secrets.html
start_sec = time.time()
for _ in range(n):
    secrets.randbits(1)
t = time.time()
run_time = (t - start_sec)
# microseconds (μs) per call
print(f"4.  {run_time / n * 1000000:.15f} ({secrets.randbits(1)}) secrets.randbits\
    \n\n                --- end ---\n")
