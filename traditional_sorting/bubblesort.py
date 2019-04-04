def bubble_sort_original(arr):
    has_changed = True

    pass_val = 1 #using to test implementation performance
    while has_changed:
        print(f"Pass: {pass_val}")
        position = 0
        has_changed = False
        while position < len(arr)-1:
            if arr[position] > arr[position+1]:
                arr[position], arr[position+1] = arr[position+1], arr[position]
                has_changed = True

            position +=1
        pass_val+=1

    print(arr)
    return arr


def bubble_sort_1(arr):
    if arr is None or len(arr) <= 1:
        return arr

    has_changed = True
    while has_changed:
        has_changed = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_changed = True

    return arr

