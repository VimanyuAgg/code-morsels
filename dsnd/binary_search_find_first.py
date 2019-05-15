def find_first(target, source):
    if source is None or len(source) == 0:
        return None

    left = 0
    right = len(source) - 1
    while left <= right:

        mid = (left + right) // 2
        if source[mid] == target:
            if (mid - 1 > 0 and source[mid - 1] < target) or mid == 0:
                return mid
            else:
                right = mid - 1
        elif source[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


multiple = [1, 1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(7, multiple))  # Should return 4
print(find_first(9, multiple))  # Should return None
print(find_first(1, multiple)) # should return 0