def binary_search(arr, n):
    '''Returns index where n is found. If n is not found, return the smallest index just bigger than n'''

    def _helper(arr, left, right, n):
        print(f"left: {left}, right:{right}")
        if left == right:
            if arr[left] >= n:
                return left

            return -1

        mid = (left + right) // 2

        if arr[mid] == n:
            return mid
        if arr[mid] > n:
            return _helper(arr, left, mid, n)

        if arr[mid] < n:
            return _helper(arr, mid + 1, right, n)

    return _helper(arr, 0, len(arr) - 1, n)




print(binary_search([1, 3, 4, 6, 7], 8))
print(binary_search([1, 3, 9, 16, 17], 8))