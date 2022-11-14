#!/usr/bin/python3

def my_factorial(x):
    return 1 if x == 0 else (x * my_factorial(x-1))
