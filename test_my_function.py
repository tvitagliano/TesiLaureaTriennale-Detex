import unittests
from FunctionExampleTest import blob_example, lazy_class_example, long_method_example, spaghetti_code_ciclomatico_example



class TestMyModule(unittest.TestCase):
    def test_spaghetti_code(self):
        result = spaghetti_code_ciclomatico_example(2, 3)
        self.assertEqual(result, 5)

    def test_blob(self):
        result = blob_example(2, 3)
        self.assertEqual(result, 5)

    def test_lazy_class(self):
        result = lazy_class_example(2, 3)
        self.assertEqual(result, 5)

    def test_long_method(self):
        result = long_method_example(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()