from src.count_dictionaries import count_dictionaries

"""
Implement a function that counts the number of dictionaries in an 
arbitrarily nested dictionary.

Example
count_dictionaries({ "a": 1 }) # 1
count_dictionaries({ "a": { "b": { "c": 1 } } }) # 3
"""

def test_returns_0_if_not_given_a_dict():
    assert count_dictionaries("ff") == 0

def test_returns_one_given_one_dict():
    assert count_dictionaries({"a": 1}) == 1

def test_counts_nested_dicts():
    assert count_dictionaries({"a": {"b": {"c": 1 }}}) == 3