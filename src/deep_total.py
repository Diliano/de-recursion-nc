def deep_total(lst):
    total = 0
    for item in lst:
        if type(item) == list:
            total += deep_total(item)
        else:
            total += item
    return total