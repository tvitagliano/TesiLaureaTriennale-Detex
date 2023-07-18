import inspect
from radon.complexity import cc_visit
#from code_smell_decorators import long_method_threshold, lazy_class_threshold, blob_method_threshold, spaghetti_code_threshold


def blob_method_threshold(max_lines):
    def decorator(func):
        def wrapper(*args, **kwargs):
            method_name = func.__name__
            source_lines = inspect.getsource(func).split('\n')
            method_length = len(source_lines)
            if method_length > max_lines:
                print(f"Avviso: Il metodo '{method_name}' supera la soglia di linee di codice consentita.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def long_method_threshold(max_length):
    def decorator(func):
        def wrapper(*args, **kwargs):
            method_name = func.__name__
            source_lines = inspect.getsource(func).split('\n')
            method_length = len(source_lines)
            if method_length > max_length:
                print(f"Avviso: Il metodo '{method_name}' supera la soglia di lunghezza massima consentita.")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def lazy_class_threshold(min_methods):
    def decorator(cls):
        if len(cls.__dict__) <= min_methods:
            print(f"Avviso: La classe '{cls.__name__}' è considerata una 'lazy class' con un numero insufficiente di metodi.")
        return cls
    return decorator

def spaghetti_code_threshold(max_complexity):
    def decorator(func):
        def wrapper(*args, **kwargs):
            method_name = func.__name__
            source_code = inspect.getsource(func)
            complexity = cc_visit(source_code)[0].complexity
            if complexity > max_complexity:
                print(f"Avviso: Il metodo '{method_name}' presenta un livello di complessità ciclomatica superiore alla soglia consentita.")
            return func(*args, **kwargs)
        return wrapper
    return decorator