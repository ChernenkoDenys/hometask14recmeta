# Напишіть метаклас, який буде перейменовувати всі атрибути, 
# назва яких починається з '__' на атрибути '__private_{attr}


class MyMetaChange(type):
    
    def __new__(cls, name, bases, attrs):
        new_attr = {}
        
        for k, v in attrs.items():
            if k.startswith("_" + name + "__"):
                new_key = k.replace("_" + name + "__", "__private_")
                new_attr[new_key] = v
            else:
                new_attr[k] = v
        return super().__new__(cls, name, bases, new_attr)

  
class MyClass(metaclass=MyMetaChange):
    
    __money = 250
    __rofl = "Rofl"
    
    def __init__(self, joke):
        self.__joke = joke
        
    def __setattr__(self, name, value):
        if name.startswith("_MyClass__"):
            name = name.replace("_MyClass__", "__private_")
            super().__setattr__(name, value)

    
instance = MyClass('lol')
print(instance.__private_rofl)
print(instance.__dict__)
print(instance.__private_joke)
