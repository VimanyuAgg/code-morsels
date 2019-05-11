import unittest
from leetcode.matrix_multiplication import matrix_multiplication2 as matrix_multiplication

class TestMatrixMultiplication(unittest.TestCase):

    def test1(self):
        m1 = [[1, 2, 3], [4, 5, 6]]
        m2 = [[7, 8], [9, 10], [11, 12]]
        self.assertEqual(matrix_multiplication(m1,m2),[[58, 64], [139, 154]])


if __name__ == "__main__":
    unittest.main()