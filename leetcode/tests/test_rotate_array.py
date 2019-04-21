import unittest
from leetcode.rotate_array import rotate


class TestRotateArray(unittest.TestCase):

    def test1(self):
        arr = [1,2,3,4,5,6]
        rotate(arr, 3)
        self.assertEqual(arr,[4,5,6,1,2,3])

    def test2(self):
        arr = [1,2,3,4,5,6]
        rotate(arr, 4)
        self.assertEqual(arr, [3,4,5,6,1,2])

    def test3(self):
        arr = [1,2,3,4,5,6]
        rotate(arr, -10)
        self.assertEqual(arr, [5,6,1,2,3,4])


    def test4(self):
        arr = [1,2,3,4,5,6]
        rotate(arr, 13)
        self.assertEqual(arr, [6,1,2,3,4,5])


    def test5(self):
        arr = [1,2,3,4,5,6]
        rotate(arr, 6)
        self.assertEqual(arr, [1,2,3,4,5,6])


if __name__ == "__main__":
    unittest.main()