import unittest
from leetcode.maxsum_subarray import maxsum_subarray


class TestMaxsumSubarray(unittest.TestCase):

    def test1(self):
        self.assertEqual(maxsum_subarray([1,2,-3,44,0,-1,10,-20]), 53)

    def test2(self):
        self.assertEqual(maxsum_subarray([]), 0)

    def test3(self):
        self.assertEqual(maxsum_subarray([-100,-3,-4,-2]), -2)


if __name__ == "__main__":
    unittest.main()