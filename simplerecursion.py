# Напишіть рекурсивну функцію, яка обчислює суму цифр заданого числа.


def recursive_sum(num: int):
    if len(str(num)) == 1:
        return num
    num_to_string = str(num)
    first_num = int(num_to_string[0])
    next_numbers = int(num_to_string[1:])
    return first_num + recursive_sum(next_numbers)


result = recursive_sum(10913) # 10
print(result)