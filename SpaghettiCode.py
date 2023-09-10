import inspect
import difflib
import ast
from radon.complexity import cc_visit
MAX_COMPLEXITY=5

#complessità
def spaghetti_code(node):
    method_complexity = calculate_complexity(node)  # Sostituisci questa funzione con il calcolo di complessità reale
            
    # Definisci il criterio per un metodo complesso
    if method_complexity > MAX_COMPLEXITY:
        return True  # Metodo considerato troppo complesso
    else:
        return False  # Metodo considerato accettabile


def calculate_complexity(node):
    complexity = 0
    for child_node in ast.walk(node):
        if isinstance(child_node, (ast.If, ast.While, ast.For)):
            complexity += 1
    
    return complexity




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
                #generate_warning("Il metodo '{}' contiene codice duplicato.".format(func.__name__))
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


