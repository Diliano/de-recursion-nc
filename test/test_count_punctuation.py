from src.count_punctuation import count_punctuation

"""
Implement a recursive function, count_punctuation, that counts the 
amount of punctuation in a string.

For this function, punctuation counts as [",", ".", "!", "?"]

Example
count_punctuation("") # 0 DONE
count_punctuation("!") # 1 DONE 
count_punctuation("What, me?") # 2
count_punctuation("Ready? Set... Go!") # 5
"""

def test_returns_0_given_empty_string():
    assert count_punctuation("") == 0

def test_handles_single_char_string():
    assert count_punctuation("!") == 1

def test_handles_multi_char_string():
    assert count_punctuation("What, me?") == 2
    assert count_punctuation("Ready? Set... Go!") == 5