import ast
import os
import csv
from LongMethod import long_method
from SpaghettiCode import spaghetti_code

def analyze_file_long(file_path, output_csv_file):
    with open(file_path, 'r') as file:
        code = file.read()
    
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if long_method(node):
                with open(output_csv_file, mode='a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([node.name, file_path, ""])

def analyze_file_spaghetti(file_path, output_csv_file):
    with open(file_path, 'r') as file:
        code = file.read()
    
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if spaghetti_code(node):
                with open(output_csv_file, mode='a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([node.name, file_path, ""])  # Metti "" come placeholder per Method Complexity

def analyze_file_blob(file_path, output_csv_file):
    with open(file_path, 'r') as file:
        code = file.read()
    
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if spaghetti_code(node):
                with open(output_csv_file, mode='a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([node.name, file_path, ""])


def analyze_file_lazy_class(file_path, output_csv_file):
    with open(file_path, 'r') as file:
        code = file.read()
    
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if spaghetti_code(node):
                with open(output_csv_file, mode='a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([node.name, file_path, ""])

def main(input_folder, output_folder):
    # Creare o aprire i file CSV per la scrittura
    long_method_csv = os.path.join(output_folder, 'longMethod.csv')
    spaghetti_code_csv = os.path.join(output_folder, 'SpaghettiCode.csv')
    blob_csv = os.path.join(output_folder, 'Blob.csv')
    lazy_class_csv = os.path.join(output_folder, 'LazyClass.csv')
        
    with open(long_method_csv, mode='w', newline='') as long_method_file, \
        open(spaghetti_code_csv, mode='w', newline='') as spaghetti_code_file, \
        open(blob_csv, mode='w', newline='') as blob_file, \
        open(lazy_class_csv, mode='w', newline='') as lazy_class_file:
        
        long_method_writer = csv.writer(long_method_file)
        long_method_writer.writerow(['Method Name', 'File Path'])
    
        spaghetti_code_writer = csv.writer(spaghetti_code_file)
        spaghetti_code_writer.writerow(['Method Name', 'File Path'])
    
        blob_writer = csv.writer(blob_file)
        blob_writer.writerow(['Method Name', 'File Path'])
    
        lazy_class_writer = csv.writer(lazy_class_file)
        lazy_class_writer.writerow(['Class Name', 'File Path'])

    
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                analyze_file_long(file_path, long_method_csv)
                analyze_file_spaghetti(file_path, spaghetti_code_csv)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 detectionDecor.py /Users/teresavitagliano/Desktop/TESI/input /Users/teresavitagliano/Desktop/TESI/output ")
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        main(input_folder, output_folder)
