def maxsum_subarray(arr):
    '''
    Assumption: Take at least one element from array
    :param arr: input array of integers - list(int/float)
    :return: maxsum of a subarray - int/float
    '''

    if not arr or isinstance(sum(arr), str):  # Check if the arr doesn't contain string elements
        return 0

    maxsum = arr[0]
    running_sum = 0

    for n in arr:
        running_sum += n

        if running_sum > maxsum:
            maxsum = running_sum

        if running_sum < 0:
            running_sum = 0

    return maxsum

