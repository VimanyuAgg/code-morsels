def bubble_sort_original(arr):
    has_changed = True

    while has_changed:
        position = 0
        has_changed = False
        while position < len(arr)-1:
            if arr[position] > arr[position+1]:
                arr[position], arr[position+1] = arr[position+1], arr[position]
                has_changed = True

            position +=1

    print(arr)
    return arr


