import unittest
from leetcode.knapsack_no_repeat import knapsack_no_repeat


class TestKnapSackNoRepeat(unittest.TestCase):

    def test1(self):
        v = [15, 10, 8, 1]
        w = [15, 12, 10, 5]

        self.assertEqual(knapsack_no_repeat(w,v, 22), 18)



if __name__ == "__main__":
    unittest.main()