import inspect


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

#@long_method_threshold(max_length=20)
#def my_function():
   #Codice della funzione