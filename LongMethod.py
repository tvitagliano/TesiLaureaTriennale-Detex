import inspect
#conteggio delle line utilizzat
MAX_STATEMENTS_THRESHOLD=5


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

def long_method(node):
    # Conta il numero di istruzioni nel corpo del metodo
    num_statements = len(node.body)
    # Definisci il criterio per un metodo troppo lungo
    if num_statements > MAX_STATEMENTS_THRESHOLD:
        return True  # Metodo considerato troppo lungo
    else:
        return False  # Metodo considerato accettabile
