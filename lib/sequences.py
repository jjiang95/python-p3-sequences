#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = [0, 1]
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print(sequence)
    else:
        i = length - 2
        while i > 0:
            sequence.append(sequence[-1] + sequence [-2])
            i -= 1
        print(sequence)
