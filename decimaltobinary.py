# Напишіть рекурсивну функцію, буде конвертувати десяткове число у двійкове.


def recursive_dec_to_bin_converter(num: int):
    if num == 1:
        return '1'
    elif num == 0:
        return '0'
    
    return recursive_dec_to_bin_converter(num//2) + str(num %2)



result = recursive_dec_to_bin_converter(12)
print(result)
