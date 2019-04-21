def rotate(arr, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    k refers to right rotation
    negative k means left rotation
    """
    if arr is None or len(arr) <= 1 or k == 0 or k == len(arr):
        return

    counter = 0
    i = 0
    while counter < len(arr):  # Runs hcf(k, len(arr)) times
        counter = migrate(i, k, arr, counter)
        i += 1


def migrate(original_index, k, arr, counter):
    n = len(arr)
    next_index = (original_index + k) % n
    elem = arr[original_index]

    while next_index != original_index:
        elem, arr[next_index] = arr[next_index], elem
        next_index = (next_index + k) % n
        counter += 1

    arr[next_index] = elem
    counter += 1
    return counter