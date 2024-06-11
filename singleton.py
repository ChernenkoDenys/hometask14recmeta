# Напишіть реалізацію патерну SIngleton за допомогою створення метакласу. 
# Сінглтон - це патерн при якому ми можемо створити лише 1 інстанс для нашого класу.

class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MySingletonExample(metaclass=Singleton):
    
    def __init__(self):
        pass
    
    
singl_1 = MySingletonExample()
singl_2 = MySingletonExample()

print(id(singl_1))
print(id(singl_2))

if singl_1 is singl_2:
    print("Singleton is correct")
else:
    print("Singleton is inccorect")