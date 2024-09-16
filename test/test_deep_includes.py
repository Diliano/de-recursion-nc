from src.deep_includes import deep_includes

"""
Implement a function that determines if a list includes a particular 
value at any level of nesting.

Example
deep_includes([1, 2], 3) # False DONE
deep_includes(["toast", ["avocado", ["chilli flakes"]]], "avocado") # True DONE

"""

def test_returns_false_given_empty_list():
    assert deep_includes([], 3) ==  False

def test_handles_single_list():
    assert deep_includes([1, 2], 2) == True
    assert deep_includes([1, 2], 3) == False

def test_handles_nested_lists():
    test_list = ["toast", ["avocado", ["chilli flakes"]]]
    test_value = "avocado"
    assert deep_includes(test_list, test_value) == True

    test_list = ["toast", ["avocado", ["chilli flakes"]]]
    test_value = "banana"
    assert deep_includes(test_list, test_value) == False