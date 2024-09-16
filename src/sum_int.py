def sum_int(num):
    if num == 0 or num == 1:
        return num
    
    return num + sum_int(num - 1)