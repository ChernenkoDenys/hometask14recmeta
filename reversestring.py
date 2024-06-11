# Напишіть рекурсивну функцію, 
# яка приймає рядок та повертає його у зворотньому порядку.


def recursive_reverse(string_to_reverse: str):
    if len(string_to_reverse) == 1:
        return string_to_reverse
    
    last_char = string_to_reverse[-1]
    return last_char + recursive_reverse(string_to_reverse[:-1])


result = recursive_reverse('hello')
print(result)