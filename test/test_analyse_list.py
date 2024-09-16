from src.analyse_list import analyse_list

"""
Write a function, analyse_list, that takes a string and an arbitrarily 
complex nested list.

It should build a dictionary where the keys are the given string and 
numbers indicating the index path to each element. The value stored on 
each key should be the value of each list element.

You can assume that the list contains only strings and other nested list.

Example
random_list = ["carrot", ["car", "boat", "plane"], "turtle", ["house"]]

analyse_list("mabel", random_list)
Should return:

{
  "mabel.0":  "carrot",
  "mabel.1.0": "car",
  "mabel.1.1" : "boat",
  "mabel.1.2": "plane",
  "mabel.2": "turtle",
  "mabel.3.0": "house"
}
"""

def test_returns_empty_dict_given_empty_list():
    assert analyse_list("impossible", []) == {}

def test_handles_single_list_with_single_element():
    assert analyse_list("mabel", ["carrot"]) == {"mabel.0": "carrot"}

def test_handles_single_list_with_multiple_elements():
    # Arrange
    test_string = "mabel"
    test_list = ["carrot", "banana", "apple"]
    expected = {"mabel.0": "carrot", "mabel.1": "banana", "mabel.2": "apple"}
    # Act
    result = analyse_list(test_string, test_list)
    # Assert
    assert result == expected

def test_handles_nested_lists():
    # Arrange
    test_string = "mabel"
    test_list = ["carrot", ["car", "boat", "plane"], "turtle", ["house"]]
    expected = {
        "mabel.0":  "carrot",
        "mabel.1.0": "car",
        "mabel.1.1" : "boat",
        "mabel.1.2": "plane",
        "mabel.2": "turtle",
        "mabel.3.0": "house"
    }
    # Act 
    result = analyse_list(test_string, test_list)
    # Assert
    assert result == expected