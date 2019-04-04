def longest_palindrome(s):

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
