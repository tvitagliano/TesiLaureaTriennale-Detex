import inspect
import difflib
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

def generate_warning(message): # type: ignore
    print("Avviso:", message)

#identificazione di duplicati 
#Viene utilizzata la libreria difflib per confrontare le linee di codice e calcolare la loro similarità.
#Se la similarità supera una soglia specificata, verrà generato un avviso indicando che il metodo contiene codice duplicato, insieme alle linee duplicate individuate.
def spaghetti_code_duplicato_threshold(max_similarity):
    def decorator(func):
        def wrapper(*args, **kwargs):
            source_code = inspect.getsource(func)
            lines = source_code.split('\n')
            duplicated_lines = find_duplicated_lines(lines, max_similarity)
            
            if duplicated_lines:
                generate_warning("Il metodo '{}' contiene codice duplicato.".format(func.__name__))
                print("Linee duplicati:")
                for line in duplicated_lines:
                    print(line)
                    
            return func(*args, **kwargs)
        return wrapper
    return decorator

def find_duplicated_lines(lines, max_similarity):
    duplicated_lines = []
    for i, line in enumerate(lines):
        for j in range(i + 1, len(lines)):
            similarity = difflib.SequenceMatcher(None, line, lines[j]).ratio()
            if similarity >= max_similarity:
                duplicated_lines.append("Linea {}: '{}'".format(i + 1, line))
                duplicated_lines.append("Linea {}: '{}'".format(j + 1, lines[j]))
    return duplicated_lines


#mancanza di chiarezza
#coesione



