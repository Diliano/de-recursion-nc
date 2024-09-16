from src.manual_reduce import manual_reduce

def test_returns_none_given_empty_iterable():
    # Arrange
    def test_func():
        pass

    test_input = []
    # Act
    result = manual_reduce(test_func, test_input)
    # Assert
    assert result == "An iterable must be provided"
    
def test_returns_first_element_given_no_initialiser_and_iterable_length_1():
    # Arrange
    def test_func():
        pass

    test_input = [2]
    # Act
    result = manual_reduce(test_func, test_input)
    # Assert 
    assert result == 2

def test_sums_a_list_of_nums():
    # Arrange
    def add_nums(num1, num2):
        return num1 + num2
    
    test_input = [1, 2, 3, 4]
    expected = 10
    # Act
    result = manual_reduce(add_nums, test_input)
    # Assert
    assert result == expected

def test_multiplies_a_list_of_nums():
    # Arrange
    def multiply_nums(num1, num2):
        return num1 * num2
    
    test_input = [1, 2, 3, 4]
    expected = 24
    # Act
    result = manual_reduce(multiply_nums, test_input)
    # Assert
    assert result == expected

def test_concatenates_strings():
    # Arrange
    def concatenate_strings(str1, str2):
        return str1 + str2
    
    test_input = ["a", "b", "c"]
    expected = "abc"
    # Act
    result = manual_reduce(concatenate_strings, test_input)
    # Assert
    assert result == expected

def test_handles_initialiser():
    # Arrange
    def add_nums(num1, num2):
        return num1 + num2
    
    test_input = [1, 2, 3, 4]
    test_initialiser = 10
    expected = 20
    # Act
    result = manual_reduce(add_nums, test_input, test_initialiser)
    # Assert
    assert result == expected

def test_returns_initialiser_if_not_none_and_iterable_is_empty():
    # Arrange
    def test_func():
        pass

    test_input = []
    test_initialiser = 10
    # Act
    result = manual_reduce(test_func, test_input, test_initialiser)
    # Assert
    assert result == 10