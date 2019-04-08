import unittest
from CTCI.ch_8_12_nQueens import solveNQueens

class TestNQueens(unittest.TestCase):

    def test1(self):
        self.assertEqual(solveNQueens(4),[[1,3,0,2],[2,0,3,1]])


if __name__ == "__main__":
    unittest.main()