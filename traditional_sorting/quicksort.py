def partition_median_of_three(array, begin, end):
    arr_3 = [array[begin],array[(begin+end)//2] ,array[end]]
    max_val = max(arr_3)
    arr_3.remove(max_val)
    print(f"max_val: {max_val}")
    min_val = min(arr_3)
    arr_3.remove(min_val)
    print(f"min_val : {min_val }")

    if max_val == min_val:
        print("high chances that the array contains same values")
    if end == array.index(max_val) and begin == array.index(min_val):
        print("high chances that array is already sorted")

    median = arr_3[0]

    array[begin], array[(begin+end)//2], array[end] = median, min_val, max_val
    pos = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pos += 1
            array[i], array[pos] = array[pos], array[i]

    array[begin], array[pos] = array[pos], array[begin]
    return pos

def quicksort_last_elem_pivot(array, begin = 0, end = None):
    if end is None:
        end = len(array) - 1

    def _inner_quicksort(array, begin, end):
        if begin >= end:
            return array

        partition = partition_last_elem_pivot(array, begin, end)
        _inner_quicksort(array, begin, partition-1)
        _inner_quicksort(array, partition + 1, end)
        return array
    return _inner_quicksort(array, begin, end)


def partition_last_elem_pivot(array, begin, end):
    array[end], array[begin] = array[begin], array[end]
    pos = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pos += 1
            array[i], array[pos] = array[pos], array[i]

    array[pos], array[begin] = array[begin], array[pos]
    return pos

def partition(array, begin, end):
    pos = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pos += 1
            array[i], array[pos] = array[pos], array[i]
    print(f"before swap arr: {array}")
    array[pos], array[begin] = array[begin], array[pos]
    print(f"after swap arr: {array}")
    return pos


def quicksort_modular(array):

    if array is None or len(array) <= 1:
        return array

    def _inner_quicksort(array, begin, end):
        # avoid checking end is None in each iteration
        if begin >= end:
            return array
        pivot = partition_median_of_three(array, begin, end)
        _inner_quicksort(array, begin, pivot-1)
        _inner_quicksort(array, pivot+1, end)
        return array

    return _inner_quicksort(array, 0, len(array) - 1)



def quicksort_original(arr, pivot_index=None, end=None):

    if pivot_index == None:
        pivot_index = 0
        end = len(arr) -1

    if pivot_index >= end:
        return arr

    pos = pivot_index
    for i in range(pivot_index + 1, end + 1):
        if arr[i] <= arr[pivot_index]:
            pos += 1
            arr[pos], arr[i] = arr[i], arr[pos]

    arr[pos], arr[pivot_index] = arr[pivot_index], arr[pos]
    quicksort_original(arr,pivot_index,pos-1)
    quicksort_original(arr,pos+1, end)
    return arr


def stable_quicksort(arr):

    if arr is None or len(arr) <= 1:
        return arr


    left, right = [], []

    pivot_index = (len(arr)-1)//2
    pivot = arr[pivot_index]  # Can choose leftmost, rightmost or median of the three elements. While choosing median as pivot,
    # care must be taken to ensure that first minimum is selected for begin and/or first max is selected for last elem

    for i in range(len(arr)):
        if arr[i] > pivot:
            right.append(arr[i])

        elif arr[i] < pivot:
            left.append(arr[i])

        else:
            # arr[i] == pivot and not the same element
            if i < pivot_index:
                left.append(arr[i])
            elif i > pivot_index:
                right.append(arr[i])

    return stable_quicksort(left) + [pivot] + stable_quicksort(right)



arr = [2,3,1,4,5]
print(stable_quicksort(arr))



