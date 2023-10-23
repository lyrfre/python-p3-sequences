#!/usr/bin/env python3

def print_fibonacci(length):
    fib_seq = []

    if length > 0:
        fib_seq.append(0)
    if length >= 2:
        fib_seq.append(1)
        for i in range(2, length):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
    print(fib_seq)

print_fibonacci(9)


def print_fib_no_range(length):
    fibo_seq = []
    if length > 0:
        fibo_seq.append(0)
        if length > 1:
            fibo_seq.append(1)
            if length >2:
                i = 2
                while i < length:
                    fibo_seq.append(
                        fibo_seq[i-1] + fibo_seq[i-2]
                    )
                    i += 1
    print(fibo_seq)

print(print_fib_no_range(9))