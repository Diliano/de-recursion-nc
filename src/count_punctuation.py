def count_punctuation(string):
    punctuations = {",", ".", "!", "?"}

    # Base case
    if len(string) == 0:
        return 0
    
    # Recursive case
    if string[0] in punctuations:
        return 1 + count_punctuation(string[1:])
    else:
        return count_punctuation(string[1:])