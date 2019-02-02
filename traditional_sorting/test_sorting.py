import unittest
from traditional_sorting.bubblesort import bubble_sort_original as bubblesort

# run as python -m traditional_sorting.test_sorting from the parent directory

class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        arr = [2,3,1,4,5]
        arr2 = [2, 3, 0, 4, -1,10]
        self.assertEqual(bubblesort(arr), sorted(arr))
        self.assertEqual(bubblesort(arr2), sorted(arr2))



if __name__ == "__main__":
    unittest.main()
