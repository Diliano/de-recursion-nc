def fib(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    
    return fib(num - 1) + fib(num - 2)