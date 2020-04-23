import fizzbuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_multiplo_de_tres(self):
        self.assertEqual(fizzbuzz.proceso(3), 'Fizz')
    def test_multiplo_de_cinco(self):
        self.assertEqual(fizzbuzz.proceso(5), 'Buzz')
    def test_multiplo_de_ambos(self):
        self.assertEqual(fizzbuzz.proceso(30), 'FizzBuzz')
    def test_resto_de_numeros(self):
        self.assertEqual(fizzbuzz.proceso(8), 8)
        self.assertEqual(fizzbuzz.proceso(17), 17)

if __name__ == '__main__':
    unittest.main()