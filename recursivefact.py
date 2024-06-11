# Напишіть рекурсивну функцію, яка обчислює факторіал заданого числа.


def recursive_factorial(num: int):
    if num < 0:
        return 0
    elif num == 0:
        return 1
    else:
        return num * recursive_factorial(num-1)


result = recursive_factorial(5)
print(result)