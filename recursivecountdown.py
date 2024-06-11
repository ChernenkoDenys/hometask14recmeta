# Напишіть рекурсивну функцію, яка повертає лічільник з числа яке ми до неї передамо до 1-го. 
# За допомогою модулю time зробіть затримку в 1 секунду між кожним повертанням лічільника.
from time import sleep


def recursive_count_down(num: int):
    sleep(1)
    
    if num == 1:
        print(num)
        return None
    else:
        print(num)
        return recursive_count_down(num-1)
        


result = recursive_count_down(10)
