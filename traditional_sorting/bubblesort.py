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


