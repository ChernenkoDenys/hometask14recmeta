# Створіть простий метаклас, який буде прінтити будь яке повідомлення, 
# коли новий клас створюється за його допомогою.


class MyMetaClass(type):
    
    def __new__(cls, name, bases, attrs):
        print("Hi, it is a new class!")
        return super().__new__(cls, name, bases, attrs)
        


class ExampleClass(metaclass=MyMetaClass):
    
    def __init__(self):
        pass
    
    