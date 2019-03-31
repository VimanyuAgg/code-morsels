import unittest
from leetcode.fruit_into_baskets import total_fruits_2 as total_fruits

class TestFruitInBaskets(unittest.TestCase):

    def test1(self):
        trees = [3,3,3,2,1,1,1,2,3,4]
        self.assertEqual(total_fruits(trees), 5)


    def test_unique(self):
        trees = [2, 3, 4]
        self.assertEqual(total_fruits(trees), 2)


    def test2(self):
        trees = [1,2,1]
        self.assertEqual(total_fruits(trees), 3)


    def test3(self):
        trees = [0,1,2,2]
        self.assertEqual(total_fruits(trees), 3)


    def test4(self):
        trees = [1,2,3,2,2]
        self.assertEqual(total_fruits(trees), 4)

    def test_len_1(self):
        trees = [1]
        self.assertEqual(total_fruits(trees), 1)


    def test5(self):
        trees = [3, 3, 3, 1, 4]
        self.assertEqual(total_fruits(trees), 4)

    def test6(self):
        trees = [0,1,6,6,4,4,6]
        self.assertEqual(total_fruits(trees), 5)

if __name__ == "__main__":
    unittest.main()
