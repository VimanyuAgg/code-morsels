def binary_search_2(arr,n):
    '''Returns the index of n if exists else -1'''

    if arr is None or len(arr) == 0:
        return -1

    def _helper(left, right):

        if left > right:
            return -1

        mid = (left+right)//2

        if arr[mid] == n:
            return mid

        elif arr[mid] > n:
            return _helper(left, mid - 1)

        elif arr[mid] < n:
            return _helper(mid + 1, right)

    return _helper(0, len(arr)-1)



"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

import math


def binary_search(input_array, value):
    """Your code goes here."""
    left = 0
    right = len(input_array) - 1

    while right >= left:
        print("** left: {}, right: {} **".format(left, right))
        # if right == left:
        #     if input_array[left] == value:
        #         return left
        #     return -1
        # mid = int(math.ceil((left + right)/2.0 - 1))
        mid = (left + right)/2
        print("mid: {}".format(input_array[mid]))
        if input_array[mid] == value:
            return mid
        elif input_array[mid] > value:
            print("mid is greater... Searching in first half")
            right = mid - 1
        else:
            print("mid is smaller... Searching in second half")
            left = mid + 1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print("*****************************")
print(binary_search(test_list, test_val2))
