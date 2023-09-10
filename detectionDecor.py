import os
from LongMethod import analyze_file_long
from SpaghettiCode import analyze_file_spaghetti
from BlobMethod import analyze_file_blob
from LazyClass import analyze_file_lazy_class


def main(input_folder, output_folder):
    for root, _, files in os.walk(input_folder):
        long_method_csv = os.path.join(output_folder, 'longMethod.csv')
        spaghetti_code_csv = os.path.join(output_folder, 'SpaghettiCode.csv')
        blob_csv = os.path.join(output_folder, 'Blob.csv')
        lazy_class_csv = os.path.join(output_folder, 'LazyClass.csv')
        
        # Elimina i file CSV se esistono
        for csv_file in [long_method_csv, spaghetti_code_csv, blob_csv, lazy_class_csv]:
            if os.path.exists(csv_file):
                os.remove(csv_file)
        
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                analyze_file_long(file_path, long_method_csv)
                analyze_file_spaghetti(file_path, spaghetti_code_csv)
                analyze_file_blob(file_path, blob_csv)
                analyze_file_lazy_class(file_path, lazy_class_csv)



if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 detectionDecor.py /Users/teresavitagliano/Desktop/TESI/input /Users/teresavitagliano/Desktop/TESI/output ")
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        main(input_folder, output_folder)

