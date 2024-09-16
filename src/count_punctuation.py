def count_punctuation(string):
    punctuations = [",", ".", "!", "?"]
    count = 0
    # Base case
    if len(string) == 0:
        return count
    
    # Recursive
    if string[0] in punctuations:
        count += 1
    
    return count + count_punctuation(string[1:])