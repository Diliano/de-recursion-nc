from src.factorial import factorial
"""
Implement a recursive function, factorial, that takes a number 
and returns the factorial of that number.

Example
factorial(0) # 1
factorial(1) # 1
factorial(2) # 2 * 1 = 2
factorial(4) # 4 * 3 * 2 * 1 = 24
"""

def test_returns_1_given_0():
    assert factorial(0) == 1

def test_returns_1_given_1():
    assert factorial(1) == 1

def test_calculates_factorial():
    assert factorial(2) == 2
    assert factorial(4) ==  24