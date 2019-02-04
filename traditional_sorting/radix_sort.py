
from collections import OrderedDict


def radix_sort(array):
    ## works with negative numbers as well all zeroes
    bucket = OrderedDict()
    for i in range(10):
        bucket[i] = []

    mod_val = 10
    div_val = 1
    need_run = {True}
    while True in need_run:
        print(f"mod_val: {mod_val}")
        need_run = {False}
        for i in array:

            if abs(i) > div_val -1:
                # we need another run if digits of any i in current run exceeds those in (mod_val -1)
                # need an extra run so that values fall into bucket[0] and bucket[9]
                # mod_val starts in 10 so chosen this
                need_run.add(True)

            val = i % mod_val
            val = val // div_val
            bucket[val].append(i)

        print(f"bucket: {bucket}")

        if not (True in need_run):
            return serialize_arr_from_dict(bucket,array,last_run=True)

        serialize_arr_from_dict(bucket, array)
        div_val *= 10
        mod_val *= 10


def serialize_arr_from_dict(bucket, array, last_run=False):
    if last_run:
        # values exist only in bucket[9] (if neg values in array) and bucket[0]
        array = bucket[9] + bucket[0]
        return array
    key = 0
    print(f"Before Serialized array: {array}")
    pointer = 0
    while pointer < len(array):
        try:
            array[pointer] = bucket[key].pop(0)
            pointer += 1
        except IndexError as e:
            key += 1

    print(f"After Serialized array: {array}")
    return array





from math import log, ceil


def getDigit(num, base, digit_num):
    # pulls the selected digit
    print(f"({num} // {base} ** {digit_num}) % {base}")
    return (num // base ** digit_num) % base


def makeBlanks(size):
    # create a list of empty lists to hold the split by digit
    return [[] for i in range(size)]


def split(a_list, base, digit_num):
    print(f"digit_num:{digit_num}")

    buckets = makeBlanks(base)
    for num in a_list:
        # append the number to the list selected by the digit
        print(f"num:{num} goes in bucket {getDigit(num, base, digit_num)}")
        buckets[getDigit(num, base, digit_num)].append(num)
    return buckets


# concatenate the lists back in order for the next step
def merge(a_list):
    # a_list are the buckets as a list of lists
    new_list = []
    print(f"before merge a_list: {a_list}, new_list: {new_list}")
    for sublist in a_list:
        new_list.extend(sublist)
    return new_list


def maxAbs(a_list):
    # largest abs value element of a list
    val= max(abs(num) for num in a_list)
    print(f"maxAbs:{val}")
    return val


def split_by_sign(a_list):
    # splits values by sign - negative values go to the first bucket,
    # non-negative ones into the second
    buckets = [[], []]
    for num in a_list:
        if num < 0:
            buckets[0].append(num)
        else:
            buckets[1].append(num)
    return buckets


def radixSort(a_list, base=10):
    # there are as many passes as there are digits in the longest number
    passes = int(round(log(maxAbs(a_list), base))+1)
    print(f"passes: {passes}")
    new_list = list(a_list)
    for digit_num in range(passes):
        a_list = merge(split(a_list, base, digit_num))
    return merge(split_by_sign(a_list))


import itertools

def radix_sort_bit_manipulation(unsorted):
    "Fast implementation of radix sort for any size num."
    maximum, minimum = max(unsorted), min(unsorted)

    max_bits = maximum.bit_length()
    highest_byte = max_bits // 8 if max_bits % 8 == 0 else (max_bits // 8) + 1

    min_bits = minimum.bit_length()
    lowest_byte = min_bits // 8 if min_bits % 8 == 0 else (min_bits // 8) + 1

    print(f"highest_byte: {highest_byte}")
    sorted_list = unsorted
    for offset in range(highest_byte):
        sorted_list = radix_sort_offset(sorted_list, offset)

    return sorted_list

def radix_sort_offset(unsorted, offset):
    "Helper function for radix sort, sorts each offset."
    byte_check = (0xFF << offset*8)

    print(f"byte check length: {byte_check.bit_length()}")
    print(f"byte_check:{byte_check}")
    buckets = [[] for _ in range(256)]

    for num in unsorted:
        byte_at_offset = (num & byte_check) >> offset*8
        print(f"(num & byte_check): {num & byte_check}")

        print(f"num: {num} goes in bucket: {byte_at_offset}")
        buckets[byte_at_offset].append(num)

    return list(itertools.chain.from_iterable(buckets))
# print(radixSort([-1,-5,-50,-50,0,2,3]))
# print(radixSort([0,0,0,0,0,0]))
# print(radixSort([1,4,5,2,3]))

#
# arr = [2,3,1,4,-5,-8]
# print(radix_sort(arr))
# print(radix_sort([-1,-5,-50,-50,0,2,3]))
# print(radix_sort([0,0,0,0,0,0]))
# print(radix_sort([-1,-1,-1,-1,-1,-1]))
# print(radix_sort([2, 3, 0, -1, -5,10]))

print(radix_sort_bit_manipulation([1,4,257,2,3]))