import inspect
from radon.complexity import cc_visit

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

#@spaghetti_code_threshold(max_complexity=10)
#def my_function():
    # Codice della funzione

