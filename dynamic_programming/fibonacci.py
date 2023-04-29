import math


def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return int((phi ** n - (1 - phi) ** n) / math.sqrt(5))


def fibonacciGenerator(n):
    if n <= 1:
        return n
    else:
        return fibonacciGenerator(n - 1) + fibonacciGenerator(n - 2)
