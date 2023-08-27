def lazy_class_threshold(min_methods):
    def decorator(cls):
        if len(cls.__dict__) <= min_methods:
            print(f"Avviso: La classe '{cls.__name__}' è considerata una 'lazy class' con un numero insufficiente di metodi.")
        return cls
    return decorator

#controlla, tramite una soglia, quanti metodi ha una classe
#ritorna un worning-avviso

def lazy_class_threshold_2(min_methods):
    def decorator(cls):
        if len(cls.__dict__) <= min_methods:
            generate_warning("La classe '{}' è considerata una 'lazy class' con un numero insufficiente di metodi.".format(cls.__name__))
        return cls
    return decorator

def generate_warning(message):
    print("Avviso:", message)