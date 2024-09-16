from src.sum_int import sum_int

"""
Implement a recursive function, sum_int, that sums the integers 1 through n.

Example
sum_int(1) # 1
sum_int(4) # 1 + 2 + 3 + 4 = 10
sum_int(10) # 55
"""

def test_returns_0_given_0():
    assert sum_int(0) == 0
    
def test_calculates_sum():
    assert sum_int(10) == 55
    assert sum_int(4) == 10