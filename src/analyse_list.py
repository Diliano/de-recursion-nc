def analyse_list(string, lst):
    dictionary = {}

    for index, item in enumerate(lst):
        if type(item) == list:
            dictionary.update(analyse_list(f"{string}.{index}", item))
        else:
            dictionary[f"{string}.{index}"] = item
    
    return dictionary