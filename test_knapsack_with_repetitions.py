import unittest
from knapsack_with_repetitions import knapsack_with_repetitions as knapsack


class TestKnapSackWithRepetitions(unittest.TestCase):

    def test_1(self):
        item_weight_val_dict = {1:1,2:5,3:5}
        max_kapsack_val = knapsack(list(item_weight_val_dict.values()),list(item_weight_val_dict.keys()),3)
        self.assertEqual(max_kapsack_val,6)


    # def test_2(self):
    #     weight_val_dict = {6:30, 3:14, 4: 16, 2: 9}
    #     max_knapsack_val = knapsack(list(weight_val_dict.values()), list(weight_val_dict.keys()), 10)
    #     self.assertEqual(max_knapsack_val, )


    def test_3(self):
        weight_val_dict = {6:30, 3:14, 4: 16, 2: 9}
        max_knapsack_val = knapsack(list(weight_val_dict.values()), list(weight_val_dict.keys()), 10)
        self.assertEqual(max_knapsack_val, 48)



if __name__ == "__main__":
    unittest.main()

