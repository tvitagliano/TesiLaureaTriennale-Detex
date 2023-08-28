import unittest
from FunctionExampleTest import blob_example, LazyClassExample, long_method_example, spaghetti_code_ciclomatico_example, spaghetti_code_duplicato_example



class TestMyModule(unittest.TestCase):
    def test_spaghetti_code(self): #OK TEST
        result = spaghetti_code_ciclomatico_example()
        self.assertEqual(result, "x è positivo"); 

    def test_spaghetti_code_duplicato(self):
        result = spaghetti_code_duplicato_example()
        self.assertEqual(result, "x è positivo")

    def test_blob(self):
        result = blob_example() 
        self.assertEqual(result, "avviso") 
        if result == "avviso":
            print(f"Avviso: Il metodo blob_example supera la soglia di linee di codice consentita.")

    def test_lazy_class(self):
        result = LazyClassExample() #il risultato genera un avviso tramite decorator
        #self.assertEqual(result, "avviso")
        
    def test_long_method(self):
        result = long_method_example() 
        self.assertEqual(result, "avviso")
        if result == "avviso":
            print(f"Avviso: Il metodo long_method_example supera la soglia di lunghezza massima consentita.")
            

if __name__ == '__main__':
    unittest.main()