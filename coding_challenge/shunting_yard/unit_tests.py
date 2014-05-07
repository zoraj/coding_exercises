import unittest
from prefixer import *

class TestPrefixer(unittest.TestCase):

    def setUp(self):
        pass

    def test_infix_to_prefix(self):
        self.assertEqual(infix_to_prefix('3'), '3')
        self.assertEqual(infix_to_prefix('1 + 1'), '(+ 1 1)')
        self.assertEqual(infix_to_prefix('2 * 5 + 1'), '(+ 1 (* 2 5))')
        self.assertEqual(infix_to_prefix('2 * ( 5 + 1 )'), '(* (+ 1 5) 2)')
        self.assertEqual(infix_to_prefix('3 * x + ( 9 + y ) / 4'), '(+ (* 3 x) (/ (+ 9 y) 4))')

if __name__ == '__main__':
    unittest.main()