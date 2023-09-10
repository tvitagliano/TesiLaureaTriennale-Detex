import inspect
import ast
import csv
#conteggio delle line utilizzat
MAX_STATEMENTS_THRESHOLD=5

def analyze_file_long(file_path, output_csv_file):
    with open(file_path, 'r') as file:
        code = file.read()
    
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if long_method(node):
                with open(output_csv_file, mode='a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    if csv_file.tell() == 0:
                        writer.writerow(['Method Name', 'File Path'])  # Scrivi l'intestazione solo se il file è vuoto
                    writer.writerow([node.name, file_path])
       

def long_method(node):
    # Conta il numero di istruzioni nel corpo del metodo
    num_statements = len(node.body)
    # Definisci il criterio per un metodo troppo lungo
    if num_statements > MAX_STATEMENTS_THRESHOLD:
        return True  # Metodo considerato troppo lungo
    else:
        return False  # Metodo considerato accettabile
