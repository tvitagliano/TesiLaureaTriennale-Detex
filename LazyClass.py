import ast
import csv

import ast

def analyze_file_lazy_class(file_path, output_csv_file):
    with open(file_path, 'r') as file:
        code = file.read()
    
    tree = ast.parse(code)
    
    class_name = None  # Inizializza il nome della classe a None
    
    # Cerca il nodo ast.ClassDef
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            break  # Esci dal ciclo dopo aver trovato la prima classe
    
    if class_name is not None:
        with open(output_csv_file, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            if csv_file.tell() == 0:
                writer.writerow(['Class Name', 'File Path'])  # Scrivi l'intestazione solo se il file è vuoto
            writer.writerow([class_name, file_path])  # Scrivi il nome della classe nel file CSV


def has_low_cohesion(class_node):
    method_names = set()

    # Raccogli i nomi dei metodi all'interno della classe
    for node in ast.walk(class_node):
        if isinstance(node, ast.FunctionDef):
            method_names.add(node.name)

    # Verifica se i metodi condividono nomi di variabili
    for method_node in class_node.body:
        if isinstance(method_node, ast.FunctionDef):
            method_locals = set()
            for node in ast.walk(method_node):
                if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                    method_locals.add(node.id)
            if method_locals & method_names:
                return True  # La classe ha bassa coesione se i metodi condividono nomi di variabili

    return False
