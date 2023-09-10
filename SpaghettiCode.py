import inspect
import difflib
import ast
import csv
from radon.complexity import cc_visit
MAX_COMPLEXITY=5


def analyze_file_spaghetti(file_path, output_csv_file):
    with open(file_path, 'r') as file:
        code = file.read()
    
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if spaghetti_code(node):
                with open(output_csv_file, mode='a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    if csv_file.tell() == 0:
                        writer.writerow(['Method Name', 'File Path'])  # Scrivi l'intestazione solo se il file è vuoto
                    writer.writerow([node.name, file_path])


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


#duplicati
def has_duplicate_lines(node):
    # Estrai il corpo del metodo
    method_body = node.body

    # Inizializza un insieme per tenere traccia delle righe viste
    seen_lines = set()

    for stmt in method_body:
        # Estrai la posizione di inizio (numero di riga) dell'istruzione
        start_line = getattr(stmt, "lineno", None)

        if start_line is not None:
            # Se hai già visto questa riga, hai trovato una linea duplicata
            if start_line in seen_lines:
                return True

            # Aggiungi la riga all'insieme delle righe viste
            seen_lines.add(start_line)

    # Nessuna linea duplicata trovata
    return False
