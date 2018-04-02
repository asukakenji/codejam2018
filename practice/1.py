# code jam: Practice Session 2018: Q1: Number Guessing

# Limits
# 1 <= T <= 20.
# A = 0. N = 30.
# Time limit: 10 seconds per test set.
# Memory limit: 1GB.
#
# Test set 1 (Visible)
# B = 30.
#
# Test set 2 (Hidden)
# B = 10**9.

import sys

def read_int():
    return int(raw_input())

def read_int_n():
    return map(int, raw_input().split())

t = read_int() # 1 <= T <= 20.
while t > 0:
    a, b = read_int_n() # A = 0.
    n = read_int() #  N = 30.
    a += 1
    while n > 0:
        q = (a + b) >> 1
        print q
        sys.stdout.flush()
        response = raw_input()
        if response == 'CORRECT':
            break
        elif response == 'TOO_SMALL':
            a = q + 1
        elif response == 'TOO_BIG':
            b = q - 1
        elif response == 'WRONG_ANSWER':
            sys.exit()
        else:
            sys.exit()
        n -= 1
    t -= 1
