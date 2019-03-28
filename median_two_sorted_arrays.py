def get_next_smallest(smaller_arr, sm_ptr, larger_arr, lg_ptr):
    if sm_ptr != len(smaller_arr) - 1 and smaller_arr[sm_ptr + 1] <= larger_arr[lg_ptr]:
        return smaller_arr[sm_ptr + 1]

    else:
        # Same return for sm_ptr == len(nums1) -1 and smaller_arr[sm_ptr+1] > larger_arr[lg_ptr]
        return larger_arr[lg_ptr]


def get_smallest_two(nums1, nums2, p1, p2):
    s1 = min(nums1[p1], nums2[p2])

    if nums1[p1] < nums2[p2]:
        return s1, get_next_smallest(nums1, p1, nums2, p2)


    else:
        return s1, get_next_smallest(nums2, p2, nums1, p1)


def findMedianSortedArrays(nums1, nums2) -> float:
    '''Returns the median of nums1 and nums2 assuming they cannot be both empty simultaneously and they are sorted '''
    '''Beats 99.73% of Leetcode solutions :D '''

    p1 = -1 if nums1 is None or len(nums1) == 0 else 0
    p2 = -1 if nums2 is None or len(nums2) == 0 else 0

    # Python3 gives integer division
    steps_to_median = (len(nums1) + len(nums2) + 1) / 2 - 1  # subtracting one gets the index

    while steps_to_median > 0.5:
        if p1 != -1 and p2 != -1:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1

        elif p1 == -1:
            p2 += 1

        elif p2 == -1:
            p1 += 1

        p1 = -1 if len(nums1) <= p1 else p1
        p2 = -1 if len(nums2) <= p2 else p2

        steps_to_median -= 1

    if steps_to_median == 0.5:
        #  Case of even number total length
        if p1 != -1 and p2 != -1:
            smallest, second_smallest = get_smallest_two(nums1, nums2, p1, p2)
            return (smallest + second_smallest) / 2

        if p1 == -1:
            return (nums2[p2] + nums2[p2 + 1]) / 2

        if p2 == -1:
            return (nums1[p1] + nums1[p1 + 1]) / 2

    if steps_to_median == 0:
        #  Case of odd number total length
        if p1 != -1 and p2 != -1:
            return min(nums1[p1] * 1.0, nums2[p2] * 1.0)

        if p1 == -1:
            return nums2[p2] * 1.0

        if p2 == -1:
            return nums1[p1] * 1.0

    # Should never happen
    return -1