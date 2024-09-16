from src.fib import fib

"""
Implement a recursive function that takes a number and returns the 
number at that point in the Fibonacci sequence. For example, fib(1) 
would return the first number in the sequence, fib(2) the second, etc.

You are not expected to come up with the Fibonacci formula yourself, 
just to implement it in Python.

In this problem, the Fibonacci sequence is as follows: 
0, 1, 1, 2, 3, 5, 8,...

Example
fib(1) # 0
fib(2) # 1
fib(7) # 8
fib(8) # 13
fib(9) # 21
"""

def test_returns_0_for_first_position():
    assert fib(1) == 0

def test_returns_1_for_second_position():
    assert fib(2) == 1

def test_calculates_fibonacci_position():
    assert fib(7) == 8
    assert fib(8) == 13
    assert fib(9) == 21