from src.sum_digits import sum_digits

"""
Implement a recursive function that sums the digits of a number until 
only one digit remains.

Example
sum_digits(11) # 2
# 1 + 1 = 2
sum_digits(99) # 9
# 9 + 9 = 18, 
# 1 + 8 = 9
"""

def test_handles_one_digit():
    assert sum_digits(2) == 2

def test_handles_two_digits():
    assert sum_digits(11) == 2
    assert sum_digits(99) == 18

def test_handles_three_digits():
    assert sum_digits(123) == 6

def test_handles_four_digits():
    assert sum_digits(1234) == 10