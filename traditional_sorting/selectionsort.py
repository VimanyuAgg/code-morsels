def selection_sort(arr):

    for i in range(len(arr)):
        min_pos = i
        for j in range(i,len(arr)):
            if arr[min_pos] > arr[j]:
                min_pos = j

        arr[i], arr[min_pos] = arr[min_pos], arr[i]

    return arr

