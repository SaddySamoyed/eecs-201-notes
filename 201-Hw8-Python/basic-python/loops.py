#!/usr/bin/env python3
import sys

# Check for at least one additional command-line argument
if len(sys.argv) < 2:
    sys.exit(1)

# Convert the 1st argument to an integer
n = int(sys.argv[1])

# While-loop to print integers from 1 to n
i = 1
while i <= n:
    print(i)
    i += 1

# For-loop with range to print integers from 1 to n
for j in range(1, n + 1):
    print(j)

 