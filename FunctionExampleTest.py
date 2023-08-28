from code_smell_decorators import blob_method_threshold, lazy_class_threshold, long_method_threshold, spaghetti_code_threshold, spaghetti_code_duplicato_threshold
#metodi che utilizziano il decorator

@spaghetti_code_threshold(max_complexity=10)
def spaghetti_code_ciclomatico_example():
    x = 5
    if x > 0:
        return "x è positivo"
    elif x < 0:
        return "x è negativo"
    else:
        for i in range(10):
            return "Iterazione", i

@spaghetti_code_duplicato_threshold(max_similarity=0.8)
def spaghetti_code_duplicato_example():
    x = 5
    if x > 0:
        return "x è positivo"
    elif x < 0:
        return "x è negativo"
    else:
        for i in range(10):
            return "Iterazione", i

            # Codice simile a quello sopra
            if x > 0:
                return "x è positivo"
            elif x < 0:
                return "x è negativo"
            else:
                for i in range(10):
                    return "Iterazione", i

@blob_method_threshold(max_lines=2)
def blob_example():
    "Linea 1"
    "Linea 2"


@long_method_threshold(max_length=10)
def long_method_example():
    "Linea 1"
    "Linea 2"
    "Linea 3"
    "Linea 4"
    "Linea 5"
    "Linea 7"
    "Linea 8"
    "Linea 9"
    "Linea 10"
    "Linea 11"
    "Linea 12"
    "Linea 13"
    "Linea 14"
    "Linea 15"
    "Linea 16"
    "Linea 17"
    "Linea 18"
    "Linea 19"
    "Linea 20"
    "Linea 21"  # Questa linea porta la lunghezza del metodo oltre la soglia


@lazy_class_threshold(min_methods=4)
class LazyClassExample:
    def method1(self):
        pass

    def method2(self):
        pass