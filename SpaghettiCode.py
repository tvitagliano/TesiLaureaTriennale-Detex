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

#complessità ciclomatica
def spaghetti_code_threshold_2(max_complexity):
    def decorator(func):
        def wrapper(*args, **kwargs):
            method_name = func.__name__
            source_code = inspect.getsource(func)
            complexity = cc_visit(source_code)[0].complexity
            if complexity > max_complexity:
                generate_warning("Il metodo '{}' ha una complessità ciclomatica superiore alla soglia consentita.".format(method_name))
            return func(*args, **kwargs)
        return wrapper
    return decorator

def generate_warning(message):
    print("Avviso:", message)

#annidamento profondo
#mancanza di chiarezza
#coesione



