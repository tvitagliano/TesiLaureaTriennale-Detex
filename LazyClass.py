def lazy_class_threshold(min_methods):
    def decorator(cls):
        if len(cls.__dict__) <= min_methods:
            print(f"Avviso: La classe '{cls.__name__}' è considerata una 'lazy class' con un numero insufficiente di metodi.")
        return cls
    return decorator


#@lazy_class_threshold(min_methods=3)
#class MyClass:
    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass

    def method4(self):
        pass
