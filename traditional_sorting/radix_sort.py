from collections import defaultdict

def radix_sort(array):
    bucket = defaultdict(list)
    val = 10
    while True:
        for i in array:
            bucket[i%val].append(i)

        if len(bucket[0]) == len(array):
            return serialize_arr_from_dict(bucket,array)

        serialize_arr_from_dict(bucket, array)
        val *= 10

def serialize_arr_from_dict(bucket, array):
    pos = 0
    for i in range(len(array)):
        try:
            array[i] = bucket[pos].pop(0)
        except IndexError as e:
            pos += 1
            array[i] = bucket[pos].pop(0)