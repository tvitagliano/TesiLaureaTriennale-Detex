import subprocess
import os
import ast
import csv
import sys
from LongMethod import long_method
#python3 decor.py decor.exe /Users/teresavitagliano/Desktop/TESI/input /Users/teresavitagliano/Desktop/TESI/output

def analyze_file(filepath, output_csv):
    with open(filepath, 'r') as file:
        source = file.read()

    tree = ast.parse(source)

    results = []

    for item in tree.body:
        if isinstance(item, ast.FunctionDef):
            method_name = item.name
            method_path = filepath
            #method_analysis = long_method(item) 

            if long_method(item):  # Analizza il metodo
                results.append((method_name, method_path))

    if results:
        file_exists = os.path.exists(output_csv)
        mode = 'a' if file_exists else 'w'
        
        with open(output_csv, mode, newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            
            if not file_exists:
                csv_writer.writerow(["Name", "File Path"])  # Header
            
            for method_name, method_path in results:
                csv_writer.writerow([method_name, method_path])
                print(f"Method '{method_name}' in '{method_path}' added to CSV")
    else:
        print("No long methods found in this file")

if __name__ == "__main__":
    executable = "/Users/teresavitagliano/Desktop/TESI/Tesi-GitHub/TesiLaureaTriennale-Detex/dist/decor"
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    output_csv = os.path.join(output_folder, "long_methods.csv")


    print(f"Executable: {executable}")
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")
    print(f"Output CSV: {output_csv}")

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                subprocess.run([executable, filepath, output_csv])
