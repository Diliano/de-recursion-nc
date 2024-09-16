def factorial(num):
    if num == 1:
        return 1
    next_step = num - 1
    return num * factorial(next_step)