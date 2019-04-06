def longest_common_substring_val(s, t):
    '''Returns the value of max common substring '''

    dp = [[0 for _ in range(len(t)+1)] for __ in range(len(s)+1)]
    max_row_index = -1
    max_substring_len = -1

    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    # max_substring_len = max(max_substring_len, dp[i][j])
                    if max_substring_len < dp[i][j]:
                        max_substring_len = dp[i][j]
                        max_row_index = i

                else:
                    dp[i][j] = 0

    if max_row_index == -1:
        return ""

    max_substring_val = s[max_row_index - max_substring_len: max_row_index]
    return max_substring_val
