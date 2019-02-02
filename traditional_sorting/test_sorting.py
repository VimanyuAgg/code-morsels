import unittest
from traditional_sorting.bubblesort import bubble_sort_original as bubblesort

# run as python -m traditional_sorting.test_sorting from the parent directory

class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        arr = [2,3,1,4,5]
        arr2 = [2, 3, 0, 4, -1,10]
        arr3 = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]
        self.assertEqual(bubblesort(arr), sorted(arr))
        self.assertEqual(bubblesort(arr2), sorted(arr2))
        self.assertEqual(bubblesort(arr3), sorted(arr3))


    def test_selection_sort(self):
        arr = [2,3,1,4,5]
        arr2 = [2, 3, 0, 4, -1,10]
        arr3 = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]
        self.assertEqual(bubblesort(arr), sorted(arr))
        self.assertEqual(bubblesort(arr2), sorted(arr2))
        self.assertEqual(bubblesort(arr3), sorted(arr3))



if __name__ == "__main__":
    unittest.main()
