# The number of inversions in a disordered list is the number of pairs of elements that are inverted (out of order) in the list.
#
# Here are some examples:
#
# [0,1] has 0 inversions
# [2,1] has 1 inversion (2,1)
# [3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
# [7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
# The number of inversions can also be thought of in the following manner.
#
# Given an array arr[0 ... n-1] of n distinct positive integers, for indices i and j,
#     if i < j and arr[i] > arr[j] then the pair (i, j) is called an inversion of arr.

# Problem statement
# Write a function, count_inversions, that takes an array (or Python list) as input, and returns a count of the total number of inversions present in the input.
#
# Mergesort provides an efficient way to solve this problem.

def count_inversions(arr):
    if not arr or len(arr) <= 1:
        return 0

    count = 0

    def _merge_sort(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        arr1 = _merge_sort(a[:mid])
        arr2 = _merge_sort(a[mid:])
        return _merge(arr1, arr2)

    def _merge(a1, a2):
        nonlocal count
        left_runner = 0
        right_runner = 0
        new_a = []
        while left_runner < len(a1) and right_runner < len(a2):
            if a1[left_runner] <= a2[right_runner]:
                new_a.append(a1[left_runner])
                left_runner += 1
            else:
                count += (len(a1) - left_runner)
                new_a.append(a2[right_runner])
                right_runner += 1

        new_a += a1[left_runner:]
        new_a += a2[right_runner:]
        return new_a

    _merge_sort(arr)
    print(f"count:{count}")
    return count

# # Working solution as well
def count_inversions2(arr,left=0,right=None ,count = 0):
    print(f"left:{left}, right:{right}, count: {count}")
    if right is None:
        right = len(arr)-1

    if left >= right:
        return count

    mid = (left+right)//2
    print(f"mid:{mid}")
    count = count_inversions2(arr, left, mid, count)
    count = count_inversions2(arr, mid+1, right, count)

    print(f"merging left:{left},left_end:{mid},right:{mid+1}, right_end:{right} ")
    count += merge_results(arr, left, mid, mid+1, right)
    print(f"returning count: {count}, arr:{arr}")
    return count


def merge_results(arr, left, left_end, right, right_end):
    left_runner = left
    right_runner = right
    count = 0
    temp_array = []

    print(f"merge_results : left:{left}, left_end:{left_end}, right:{right}, right_end:{right_end}")
    print(f"arr:{arr}")
    while (left_runner <= left_end) and (right_runner <= right_end):
        print(f"left_runner:{left_runner}, right_runner:{right_runner}")
        if arr[left_runner] <= arr[right_runner]:
            temp_array.append(arr[left_runner])
            left_runner += 1
        else:
            print(f"count to be increased from {count}->{count+ left_end - left_runner+1}")
            count += (left_end - left_runner +1)
            print(f"new_count:{count}")
            temp_array.append(arr[right_runner])
            right_runner += 1

        if left_runner > left_end:
            while right_runner <= right_end:
                temp_array.append(arr[right_runner])
                right_runner += 1
            break

        if right_runner > right_end:
            while left_runner <= left_end:
                temp_array.append(arr[left_runner])
                left_runner += 1

            break

    i = 0
    for index in range(left,right_end+1):
        arr[index] = temp_array[i]
        i += 1

    return count


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")


arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)
print(arr)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)