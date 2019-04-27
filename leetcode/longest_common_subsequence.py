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
    return lcs[len(arr2)][len(arr1)], lcs


def backtrack_common_subsequence(arr1, arr2):

    len_lcs, lcs = longest_common_subsequence(arr1, arr2)

    if len_lcs == 0:
        return ""

    res = ""
    i = len(arr2)  # lcs has rows of len(arr2)
    j = len(arr1)  # lcs has cols of len(arr1)
    while len_lcs > 0:

        # print(f"len_lcs: {len_lcs}")
        if arr2[i-1] == arr1[j-1]:
            res = arr1[j-1]+res
            i -= 1
            j -= 1
            len_lcs -= 1

        else:
            if lcs[i][j] == lcs[i-1][j]:
                i -= 1

            elif lcs[i][j] == lcs[i][j-1]:
                j -= 1

            else:
                print(f"there is some issue in lcs dp array! at [{i}][{j}]")

        if i < 0 or j < 0:
            print("len_lcs isn't properly computed")

    print(res)
    return res
