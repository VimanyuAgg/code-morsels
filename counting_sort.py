def counting_sort(arr):
    '''no element of array can be negative or fraction'''
    count_arr = [0]*(max(arr)+1)
    for i in arr:
        count_arr[i] += 1

    pos = 0
    result = [0]*len(arr)
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            result[pos] = i
            pos += 1

    return result

def counting_sort_stable(arr):
    count_arr = [0]* (max(arr)+1)
    for i in arr:
        count_arr[i] += 1

    pos_arr = [0]*len(count_arr)
    for i in range(1,len(count_arr)):
        pos_arr[i] = pos_arr[i-1] + count_arr[i-1] # where will the ith value start in result array

    # print(pos_arr)
    result = [0]*len(arr)
    # print(len(arr))
    print("******")
    for i in range(len(arr)):
        result[pos_arr[arr[i]]] = arr[i]
        pos_arr[arr[i]] += 1
    return result

print(counting_sort([4,2,3,4,4,1,1,6,6,5,0,0,10]))
print(counting_sort_stable([4,2,3,4,4,1,1,6,6,5,0,0,10]))