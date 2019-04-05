
def insertion_sort(arr):
    for i in range(1,len(arr)):
        prev = i-1
        need_shift = False
        while arr[i] < arr[prev] and prev >= 0:
            prev = prev -1
            need_shift = True

        if need_shift:
            val = arr[i]
            for j in range(i, prev +1, -1):
                # we want to shift elements from prev + 1 to i (both included)
                arr[j] = arr[j-1]

            arr[prev+1] = val

    return arr

def insertion_sort_2(lst):
    #timeit shows it's better

    if lst is None or len(lst)  <= 1:
        return lst

    for index in range(1, len(lst)):

        currentvalue = lst[index]
        position = index

        while position > 0 and lst[position - 1] > currentvalue:
            lst[position] = lst[position - 1]
            position = position - 1

        lst[position] = currentvalue
    return lst


# lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# insertionSort(lst)
# print(lst)

# arr = [2,3,1,4,5]
#
# print(insertion_sort(arr))

