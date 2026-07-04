import unittest
from src.calculator import sumar, rest

class testCalculator(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(5,3),8)
        self.assertEqual(sumar(-1,1),0)
        self.assertEqual(sumar(0,0),0)

    def test_rest(self):
        self.assertEqual(rest(5,3), 2)
        self.assertEqual(rest(-1,-1), 0)
        self.assertEqual(rest(0,5), -5)


if __name__ == '__main__':
    unittest.main()


        