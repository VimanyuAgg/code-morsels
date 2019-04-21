def longest_increasing_subsequence(arr):
    if arr is None or len(arr) == 0:
        return 0

    sub_arr = []
    res = 0

    for i in range(len(arr)):
        lis_len_ending_i_including_arri = 0

        for j in range(i):
            if arr[j] < arr[i] and sub_arr[j] > lis_len_ending_i_including_arri:
                lis_len_ending_i_including_arri = sub_arr[j]

        sub_arr.append(lis_len_ending_i_including_arri + 1)  # lis_len for this shorter array includes arr[i] so adding 1
        res = max(res,lis_len_ending_i_including_arri + 1)

    return res