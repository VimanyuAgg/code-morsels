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

wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
def bubble_sort_2(arr):
    # TODO: Implement bubble sort solution
    if not arr or len(arr) == 0:
        return arr
    has_changed = True
    end_pos = len(arr) - 1
    while has_changed:
        has_changed = False
        pos = 0
        while pos < end_pos:
            if arr[pos] > arr[pos+1]:
                arr[pos], arr[pos+1]= arr[pos+1], arr[pos]
                has_changed = True
            pos += 1
        end_pos -= 1 # save some comparisions for the next turn as we know last elements are in correct place
    return

bubble_sort_1(wakeup_times)
print(wakeup_times)
print("Pass" if (wakeup_times[0] == 3) else "Fail")
