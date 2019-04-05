def merge_sort_original(arr):
    if arr is None or len(arr) <= 1:
        return arr
    mid = len(arr)//2
    print ("**************")
    print(f"current array:{arr}")
    print(f"mid is {mid}")
    arr1 = merge_sort_original(arr[:mid])
    print(f"arr[:mid+1] on {arr[:mid]} is {arr1}")
    arr2 = merge_sort_original(arr[mid:])
    print(f"arr[mid+1:] on {arr[mid:]} is {arr2}")

    return merge_after2(arr1, arr2)

def merge_after2(arr1, arr2):
    result = []
    p1 = 0
    p2 = 0

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] <= arr2[p2]:
            result.append(arr1[p1])
            p1 +=1
        else:
            result.append(arr2[p2])
            p2 +=1

    result += arr1[p1:]  # Easier to ask forgiveness than permission
    result += arr2[p2:]
    return result


def merge_1(arr1, arr2):
    print(f"merge on {arr1} and {arr2}")

    result = []
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    p1 = 0
    p2 = 0

    while (p1 < arr1_len) or (p2 < arr2_len):
        if p1 >= arr1_len:
            result += arr2[p2:]
            break

        if p2 >= arr2_len:
            result += arr1[p1:]
            break


        if arr1[p1] <= arr2[p2]:
            result.append(arr1[p1])
            p1 +=1

        else:
            result.append(arr2[p2])
            p2 +=1

    # print(f"result array: {result}")
    return result

def merge_original(arr1, arr2):
    print(f"merge on {arr1} and {arr2}")

    result = []
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    p1 = 0
    p2 = 0

    while (p1 < arr1_len) or (p2 < arr2_len):
        if p1 >= arr1_len:

            while p2 < arr2_len:
                result.append(arr2[p2])
                p2 += 1
            break

        if p2 >= arr2_len:
            while p1 < arr1_len:
                result.append(arr1[p1])
                p1 += 1
            break


        if arr1[p1] <= arr2[p2]:
            result.append(arr1[p1])
            p1 +=1

        else:
            result.append(arr2[p2])
            p2 +=1

    # print(f"result array: {result}")
    return result


# print(merge_sort_original([2,3,1,4,5]))