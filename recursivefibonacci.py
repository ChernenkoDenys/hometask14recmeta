# Напишіть рекурсивну функцію, яка знаходить n-не число послідовності фібоначчі.


def recursive_fibonnaci(num: int):
    if num == 0:
        return 0
    elif num <= 2:
        return 1

    return recursive_fibonnaci(num-2) + recursive_fibonnaci(num-1) 
    


result = recursive_fibonnaci(10) # 55
print(result)