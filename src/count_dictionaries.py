def count_dictionaries(dictionary):
    if type(dictionary) != dict:
        return 0
    
    count = 1

    for item in dictionary:
        if type(dictionary[item]) == dict:
            count += count_dictionaries(dictionary[item]) 
    return count

