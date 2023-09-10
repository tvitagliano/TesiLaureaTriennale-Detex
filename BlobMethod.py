import inspect


#controllo delle linee di un metodo
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


