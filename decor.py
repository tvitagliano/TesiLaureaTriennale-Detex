#!/usr/bin/python3

import subprocess
import os
import ast
import csv
import sys
from LongMethod import long_method
#python3 decor.py /Users/teresavitagliano/Desktop/TESI/input /Users/teresavitagliano/Desktop/TESI/output

class MethodVisitor(ast.NodeVisitor):
    def __init__(self):
        self.methods = []

    def visit_FunctionDef(self, node):
        method_name = node.name
        method_start_line = node.lineno
        method_end_line = node.end_lineno

        # Verifica se il metodo è troppo lungo utilizzando il metodo long_method
        if long_method(node): 
            self.methods.append((method_name, method_start_line, method_end_line))

        self.generic_visit(node)

def analyze_method(filepath):
    with open(filepath, 'r') as file:
        source_code = file.read()
        tree = ast.parse(source_code)

    # Crea un visitor per identificare i metodi
    visitor = MethodVisitor()
    visitor.visit(tree)

    # Ora visitor.methods conterrà una lista di tuple (nome del metodo, riga di inizio, riga di fine)
    return visitor.methods


def main():
    if len(sys.argv) < 4:
        print("Usage: {} <executable_path> <input_folder> <output_folder>".format(sys.argv[0]))
        sys.exit(1)

    executable = sys.argv[1]
    input_folder = sys.argv[2]
    output_folder = sys.argv[3]
    output_csv = os.path.join(output_folder, "long_methods.csv")

    print(f"Executable: {executable}")
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")
    print(f"Output CSV: {output_csv}")

    # Crea un file CSV per i metodi lunghi
    with open(output_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Method Name", "File Path"])
        # Scorrere i file Python nella cartella di input
        for root, _, files in os.walk(input_folder):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)

                    # Analizza il metodo e verifica se è lungo
                    methods = analyze_method(filepath)
                    for method in methods:
                        method_name, method_start_line, method_end_line = method
                        csv_writer.writerow([method_name, filepath])

    # Esegui l'eseguibile specificato con gli argomenti necessari
    subprocess.run([executable, input_folder, output_folder])

if __name__ == "__main__":
    main()