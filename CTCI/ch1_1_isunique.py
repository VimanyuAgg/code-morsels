def is_unique(arr):
    '''
    Checks if the input array has all unique elements
    :param arr: iterable
    :return: Bool
    '''

    if not arr:
        return True

    buff = 0  # Initialize to int

    for a in arr:
        ord_a = ord(a)
        if (1 << ord_a) & buff > 0:
            return False
        buff |= (1 << ord_a)

    return True




