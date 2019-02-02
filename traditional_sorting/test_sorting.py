import unittest
from timeit import default_timer as timer
import copy
from traditional_sorting.bubblesort import bubble_sort_original as bubblesort
from traditional_sorting.selectionsort import selection_sort as selectionsort
from traditional_sorting.insertion_sort import insertion_sort as insertionsort, insertion_sort_2 as insertionsort2
from traditional_sorting.mergesort import  merge_sort_original as mergesort
from traditional_sorting.quicksort import quicksort_modular as quicksort
from traditional_sorting.radix_sort import radix_sort as radixsort

# run as python -m traditional_sorting.test_sorting from the parent directory

class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        arr = [2,3,1,4,5]
        arr2 = [2, 3, 0, 4, -1,10]
        arr3 = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]

        arr_test = copy.deepcopy(arr)
        arr_test2 = copy.deepcopy(arr2)
        arr_test3 = copy.deepcopy(arr3)
        self.assertEqual(bubblesort(arr), sorted(arr_test))
        self.assertEqual(bubblesort(arr2), sorted(arr_test2))
        self.assertEqual(bubblesort(arr3), sorted(arr_test3))


    def test_selection_sort(self):
        arr = [2,3,1,4,5]
        arr2 = [2, 3, 0, 4, -1,10]
        arr3 = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]
        arr_test = copy.deepcopy(arr)
        arr_test2 = copy.deepcopy(arr2)
        arr_test3 = copy.deepcopy(arr3)

        self.assertEqual(selectionsort(arr), sorted(arr_test))
        self.assertEqual(selectionsort(arr2), sorted(arr_test2))
        self.assertEqual(selectionsort(arr3), sorted(arr_test3))

    def test_insertion_sort(self):
        arr = [2,3,1,4,5]
        arr2 = [2, 3, 0, 4, -1,10]
        arr3 = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]
        arr_test = copy.deepcopy(arr)
        arr_test2 = copy.deepcopy(arr2)
        arr_test3 = copy.deepcopy(arr3)
        start1 = timer()
        self.assertEqual(insertionsort(arr), sorted(arr_test))
        end1 =  timer()
        self.assertEqual(insertionsort(arr2), sorted(arr_test2))
        end2 = timer()
        self.assertEqual(insertionsort(arr3), sorted(arr_test3))
        end3 = timer()
        print("original for arr {}: {}".format(arr_test,end1-start1))
        print("original for arr2 {}: {}".format(arr_test2, end2 - end1))
        print("original for arr3 {}: {}".format(arr_test3, end3 - end2))

        start2 = timer()
        self.assertEqual(insertionsort2(arr), sorted(arr_test))
        end4 = timer()
        self.assertEqual(insertionsort2(arr2), sorted(arr_test2))
        end5 = timer()
        self.assertEqual(insertionsort2(arr3), sorted(arr_test3))
        end6 = timer()
        print("after for arr {}: {}".format(arr_test, end4 - start2))
        print("after for arr2 {}: {}".format(arr_test2, end5 - end4))
        print("after for arr3 {}: {}".format(arr_test3, end6 - end5))

    def test_merge_sort(self):
        arr = [2,3,1,4,5]
        arr2 = [2, 3, 0, 4, -1,10]
        arr3 = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]
        arr_test = copy.deepcopy(arr)
        arr_test2 = copy.deepcopy(arr2)
        arr_test3 = copy.deepcopy(arr3)

        self.assertEqual(mergesort(arr), sorted(arr_test))
        self.assertEqual(mergesort(arr2), sorted(arr_test2))
        self.assertEqual(mergesort(arr3), sorted(arr_test3))

    def test_quicksort(self):
        arr = [2,3,1,4,5]
        arr2 = [2, 3, 0, 4, -1,10]
        arr3 = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]
        arr_test = copy.deepcopy(arr)
        arr_test2 = copy.deepcopy(arr2)
        arr_test3 = copy.deepcopy(arr3)

        self.assertEqual(quicksort(arr), sorted(arr_test))
        self.assertEqual(quicksort(arr2), sorted(arr_test2))
        self.assertEqual(quicksort(arr3), sorted(arr_test3))


    def test_radixsort(self):
        arr = [2,3,1,4,5]
        arr2 = [2, 3, 0, 4, -1,10]
        arr3 = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18]
        arr_test = copy.deepcopy(arr)
        arr_test2 = copy.deepcopy(arr2)
        arr_test3 = copy.deepcopy(arr3)

        self.assertEqual(quicksort(arr), sorted(arr_test))
        self.assertEqual(quicksort(arr2), sorted(arr_test2))
        self.assertEqual(quicksort(arr3), sorted(arr_test3))


if __name__ == "__main__":
    unittest.main()
