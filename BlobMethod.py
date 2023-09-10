import inspect
import ast
import csv

def analyze_file_blob(file_path, output_csv_file):
    with open(file_path, 'r') as file:
        code = file.read()
    
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if depends_on_external_variables(node):
                with open(output_csv_file, mode='a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    if csv_file.tell() == 0:
                        writer.writerow(['Method Name', 'File Path'])  # Scrivi l'intestazione solo se il file è vuoto
                    writer.writerow([node.name, file_path])



#Dipendenza da Variabili Esterne
def depends_on_external_variables(node):
    external_variables = set()

    def visit(node):
        if isinstance(node, ast.Name):
            if node.id not in local_variables:
                external_variables.add(node.id)
        for child_node in ast.iter_child_nodes(node):
            visit(child_node)

    local_variables = set()
    for arg in node.args.args:
        local_variables.add(arg.arg)

    visit(node)

    return len(external_variables) > 0
