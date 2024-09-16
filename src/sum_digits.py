def sum_digits(num):
    # Base case
    if num == 0:
        return num

    # Recursive 
    return (num % 10) + sum_digits(num // 10) 