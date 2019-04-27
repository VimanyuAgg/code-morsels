def longest_common_subsequence(arr1, arr2):

    if (not arr1) or (not arr2):
        return 0

    lcs = [[0 for _ in range(len(arr1) + 1)] for __ in range(len(arr2) + 1)]

    for i in range(1, len(arr2)+1):  # !Important (arr2 instead of arr1, start and end with +1)
        for j in range(1, len(arr1)+1):
            if arr2[i-1] == arr1[j-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]

            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    print(lcs)
    return lcs[len(arr2)][len(arr1)]

