import unittest

from knapsack_without_repetitions import knapsack_without_repetitions_recursive, knapsack_without_repetitions_dynamic

class TestKnapsackWithoutReps(unittest.TestCase):

    def test1_happyflow(self):
        w_arr = [2, 3, 4, 6]
        val_arr = [9, 14, 16, 30]
        capacity = 10
        self.assertEqual(knapsack_without_repetitions_recursive(capacity,w_arr,val_arr),46)


    def test2_happyflow(self):
        w_arr = [2, 3, 4, 6]
        val_arr = [9, 14, 16, 30]
        capacity = 10
        self.assertEqual(knapsack_without_repetitions_dynamic(capacity,w_arr,val_arr),46)


if __name__ == "__main__":
    unittest.main()
