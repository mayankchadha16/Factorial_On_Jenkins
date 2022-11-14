# Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    return 1 if x == 0 else (x * factorial(x-1))
