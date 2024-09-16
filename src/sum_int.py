def sum_int(num):
    if num == 0:
        return 0
    
    if num == 1:
        return 1
    
    step_num = num - 1
    return num + sum_int(step_num)