#!/bin/python

# Usage:
# `python extended_euclid.py a n`
# where
# `a` is the element whose multiplicative inverse we are calculating
# `n` is the modular base
#
# Output:
# - prints a table showing each step of the extended euclid algorithm
# - prints the modular inverse of `a`. formally, `t` s.t. `t ===`

# Requires python 3.6+
# Based on pseudocode from https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers

import sys

def print_table(lists):
    max_list_length = len(max(lists, key = lambda l: len(l)))
    for i in range(0, max_list_length):
        line = ""
        for l in lists:
            item = l[i] if i < len(l) else ""
            line += f"{item}\t"

        print(line)

def inverse(a, n):
    (t, newt) = (0, 1)
    (r, newr) = (n, a)

    t_list = ["t", t, newt]
    r_list = ["r" , r, newr]
    quotient_list = ["q"]

    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt) 
        (r, newr) = (newr, r - quotient * newr)

        r_list += [newr]
        t_list += [newt]
        quotient_list += [quotient]

    print_table([r_list, t_list, quotient_list])

    if r > 1: 
        return "a is not invertible"
    if t < 0:
        t = t + n
    return t

if __name__ == "__main__":
    a = int(sys.argv[1])
    n = int(sys.argv[2])

    print(f"a = {a}\tn = {n}\n")
    result = inverse(a, n)
    print(f"\nInverse: {result}")