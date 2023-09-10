#
def lazy_class_threshold(min_methods):
    def decorator(cls):
        if len(cls.__dict__) <= min_methods:
            print(f"Avviso: La classe '{cls.__name__}' è considerata una 'lazy class' con un numero insufficiente di metodi.")
        return cls
    return decorator


#controlla, tramite una soglia, quanti metodi ha una classe
#ritorna false altrimenti

