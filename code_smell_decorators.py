import inspect
import difflib
from radon.complexity import cc_visit
#from code_smell_decorators import long_method_threshold, lazy_class_threshold, blob_method_threshold, spaghetti_code_threshold


#complessità, grandezza
def blob_method_threshold(max_lines):
    def decorator(func):
        def wrapper(*args, **kwargs):
            method_name = func.__name__
            source_lines = inspect.getsource(func).split('\n')
            method_length = len(source_lines)
            if method_length > max_lines:
                return "avviso"
            return func(*args, **kwargs)
        return wrapper
    return decorator

#lunghezza di un metodo 
def long_method_threshold(max_length):
    def decorator(func):
        def wrapper(*args, **kwargs):
            method_name = func.__name__
            source_lines = inspect.getsource(func).split('\n')
            method_length = len(source_lines)
            if method_length > max_length:
                return "avviso"
            return func(*args, **kwargs)
        return wrapper
    return decorator

#numero di metodi all'interno di una classe
def lazy_class_threshold(min_methods):
    def decorator(cls):
        if len(cls.__dict__) <= min_methods:
            print(f"Avviso: La classe '{cls.__name__}' è considerata una 'lazy class' con un numero insufficiente di metodi.")
        return cls
    return decorator

#calcolo della complessità ciclomatica
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

def generate_warning(message):
    print("Avviso:", message)