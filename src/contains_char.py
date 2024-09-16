def contains_char(string, char):
    string = string.lower()
    char = char.lower()
    # Base case
    if len(string) == 0:
        return False
    if string[0] == char:
        return True
    
    # Recursive case
    return contains_char(string[1:], char)