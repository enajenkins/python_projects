# On a piano, a key has a frequency, say f0.
# Each higher key (black or white) has a frequency of f0 * r to the n power, 
# where n is the distance (number of keys) from that key,
# and r is 2(1/12).
# To compute the next 3 higher key frequencies, use one statement to compute r = 2(1/12) using the pow function
# (remember to import the math module). Then use that r in subsequent statements 
# that use the formula fn = f0 * rn with n being 1, 2, and finally 3.

import math

initial_freq = float(input())
r = math.pow(2, 1/12)
n = 1
next_higher_key = initial_freq * math.pow(r, n)

print(f"{initial_freq:.2f} Hz")

# Given an initial key frequency, output that frequency and the next 3 higher key frequencies.

print(f"{next_higher_key:.2f} Hz")

n = 2
next_higher_key = initial_freq * math.pow(r, n)
print(f"{next_higher_key:.2f} Hz")

n = 3
next_higher_key = initial_freq * math.pow(r, n)
print(f"{next_higher_key:.2f} Hz")

