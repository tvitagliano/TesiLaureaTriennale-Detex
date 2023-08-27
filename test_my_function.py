import unittest
from FunctionExampleTest import blob_example, LazyClassExample, long_method_example, spaghetti_code_ciclomatico_example



class TestMyModule(unittest.TestCase):
    def test_spaghetti_code(self):
        result = spaghetti_code_ciclomatico_example()
        self.assertEqual(result, 0)

    def test_blob(self):
        result = blob_example()
        self.assertEqual(result, 0)

    def test_lazy_class(self):
        result = LazyClassExample()
        self.assertEqual(result, 0)

    def test_long_method(self):
        result = long_method_example()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()