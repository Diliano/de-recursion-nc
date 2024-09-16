def manual_reduce(func, iterable, initialiser=None):
    if not iterable and initialiser == None:
        return "An iterable must be provided"
    elif not iterable:
        return initialiser
    
    if len(iterable) == 1:
        return iterable[0]
    
    result = iterable[0] if initialiser == None else initialiser

    if initialiser == None:
        for i in range(1, len(iterable)):
            result = func(result, iterable[i])
    else:
        for i in range(0, len(iterable)):
            result = func(result, iterable[i])

    return result