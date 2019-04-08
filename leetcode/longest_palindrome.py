def longest_palindromic_substring_dp(s):

    if s is None or len(s) <= 0:
        return ""
    dp = [[False for _ in range(len(s))] for __ in range(len(s))]
    start = 0
    end = 0
    for i in range(len(s)):
        for j in range(i, -1, -1):
            if s[i] == s[j] and (i - j < 3 or dp[i - 1][j + 1]):
                dp[i][j] = True
                if i - j >= end - start:
                    end, start = i, j
                    # print(f"start:{start}, end:{end}")
    # print(dp)
    return s[start:end + 1]



def longest_palindrome_original(s):

    if s is None or len(s) == 0:
        return ""

    res = ""
    end = len(s) - 1

    start = 0
    while start < end:
        curr_end = end
        while start < curr_end:
            # print(f"checking string:{s[start:curr_end+1]}")
            if s[start] == s[curr_end]:
                if check_palindrome(s, start, curr_end) and len(res) < (curr_end - start + 1):
                    # print("palindrome!")
                    res = s[start: curr_end+1]
                    # print(res)
                    break  # subsequent palindromes, if any, in s[start:curr_end] will be less in len than current res

            curr_end -= 1

        start += 1

    if len(res) == 0:
        return s[0]  # smallest longest_palindrome is always one
    else:
        # print(res)
        return res


def check_palindrome(s,start,end):
    # print(f"check_palindrome for s:{s}")
    if start >= end:
        return True

    if s[start] == s[end]:
        return check_palindrome(s, start+1, end-1)

    else:
        return False
