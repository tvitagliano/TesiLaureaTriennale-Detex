from code_smell_decorators import blob_method_threshold, lazy_class_threshold, long_method_threshold, spaghetti_code_threshold
#metodi che utilizziano il decorator

@spaghetti_code_threshold(max_complexity=10)
def spaghetti_code_ciclomatico_example():
    x = 5
    if x > 0:
        print("x è positivo")
    elif x < 0:
        print("x è negativo")
    else:
        for i in range(10):
            print("Iterazione", i)



@blob_method_threshold(max_lines=2)
def blob_example():
    print("Linea 1")
    print("Linea 2")


@long_method_threshold(max_length=10)
def long_method_example():
    print("Linea 1")
    print("Linea 2")
    print("Linea 3")
    print("Linea 4")
    print("Linea 5")
    print("Linea 6")
    print("Linea 7")
    print("Linea 8")
    print("Linea 9")
    print("Linea 10")
    print("Linea 11")
    print("Linea 12")
    print("Linea 13")
    print("Linea 14")
    print("Linea 15")
    print("Linea 16")
    print("Linea 17")
    print("Linea 18")
    print("Linea 19")
    print("Linea 20")
    print("Linea 21")  # Questa linea porta la lunghezza del metodo oltre la soglia


@lazy_class_threshold(min_methods=3)
class LazyClassExample:
    def method1(self):
        pass

    def method2(self):
        pass