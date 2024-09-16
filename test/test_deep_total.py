from src.deep_total import deep_total

"""
Implement a function that totals an arbitrarily nested list of integers.

Example
deep_total([1, 2, 3]) # 6 DONE
deep_total([1, [5, 10]]) # 16 DONE
deep_total([3, [[6]], 9]) # 18 DONE
"""

def test_returns_0_given_empty_list():
    assert deep_total([]) == 0

def test_handles_single_list():
    assert deep_total([1, 2, 3]) == 6

def test_handles_one_nested_list():
    assert deep_total([1, [5, 10]]) == 16 

def test_handles_multi_nested_list():
    assert deep_total([3, [[6]], 9]) == 18