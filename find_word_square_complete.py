from collections import defaultdict
def part1_is_word_square(arr):
    arr_len = len(arr)
    def all_len_equal():
        for word in arr:
            if len(word) != arr_len:
                return False
        return True

    ## arr has to be nxn matrix i.e. all length should be equal
    if not all_len_equal():
        return False

    ## All words are now equal length
    for r in range(arr_len):
        for c in range(r+1, arr_len):
            if arr[r][c] != arr[c][r]:
                return False

    return True


def sanitize(words):
    ## Checks if there are atleast some words of same length for which #such words = length of #such words
    word_dict = defaultdict(list)
    for w in words:
        word_dict[len(w)].append(w)

    good_list = [same_len_words_list for word_len,same_len_words_list in word_dict if word_len == len(same_len_words_list)]
    return good_list

def part2_find_all_word_squares(words):
    if len(words) <= 1:
        return words

    good_list = sanitize(words)
    if len(good_list) == 0:
        return []

    final_output = []
    for equal_len_words_list in good_list:
        final_output.append(find_word_squares(equal_len_words_list))

    return final_output

def find_word_squares(word_list):
    # Now all word in words are of same length and size of words is also equal to len(words)
    len_word_list = len(word_list)
    output = []
    prefix_dict = defaultdict(set) #Need a list in case duplicates are allowed # Would also need to sanitize final output for dups
    for word in word_list:
        for i in range(len(word)):
            prefix_dict[word[:i+1]].add(word)

    for word in word_list:
        candidate = helper([word], prefix_dict, len_word_list)
        if len(candidate) != len_word_list:
            continue
        output.append(candidate)
    return output

def helper(arr, prefix_dict, n):
    if len(arr) == n:
        return arr

    prefix = ''
    prefix_index = len(arr)
    for a in arr:
        prefix += a[prefix_index]

    #can also write prefix = ''.join(list(zip(*arr)[len(arr)])
    if prefix in prefix_dict:
        helper(arr+[prefix_dict[prefix]], prefix_dict, n)
    else:
        return []
