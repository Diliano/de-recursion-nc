def deep_includes(lst, value):
    for item in lst:
        if item == value:
            return True
        elif type(item) == list:
            return deep_includes(item, value)
    return False