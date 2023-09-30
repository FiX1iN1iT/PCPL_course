import unittest
from main import *

class Test_biquadrate_solution(unittest.TestCase):
    def test_0_roots(self):
        self.assertEqual(len(solve_biquadrate_equation(1, 0, 10)), 0)
    def test_2_roots(self):
        self.assertEqual(len(solve_biquadrate_equation(1, 0, -4)), 2)
        self.assertEqual(solve_biquadrate_equation(1, 0, -4), [1.4142135623730951, -1.4142135623730951])
    def test_3_roots(self):
        self.assertEqual(len(solve_biquadrate_equation(-4, 16, 0)), 3)
        self.assertEqual(solve_biquadrate_equation(-4, 16, 0), [0.0, 2.0, -2.0])
    def test_4_roots(self):
        self.assertEqual(len(solve_biquadrate_equation(1, -13, 36)), 4)
        self.assertEqual(solve_biquadrate_equation(1, -13, 36), [3.0, -3.0, 2.0, -2.0])


if __name__ == '__main__':
    unittest.main()
