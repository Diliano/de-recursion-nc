from src.contains_char import contains_char

"""
Implement a recursive function, contains_char, that takes a string 
and a single character as inputs. The function should return a boolean 
stating if the character is present in the string.

Example
contains_char("h", "h") # True
contains_char("eggy bread", "y") # True
contains_char("mick's sick", "j") # False

Bonus Points
Make your function case-insensitive:

Example
contains_char("Cheddar or Wensleydale?", "w") # True
"""

def test_handles_one_char_input():
    assert contains_char("h", "h") == True

def test_handles_multi_char_input():
    assert contains_char("eggy bread", "y") == True

def test_returns_false_if_char_not_present():
    assert contains_char("mick's sick", "j") == False

def test_handles_empty_string():
    assert contains_char("", "y") == False

def test_ignores_case():
    assert contains_char("Cheddar or Wensleydale?", "w") == True