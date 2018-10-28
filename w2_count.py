def check(c):
    if (ord(c) < 65) or (90 < ord(c) < 97) or (ord(c) > 122):
        return True
    return False


def check_punc_convert_lower(word):
    word = word.lower()
    if check(word[-1]):  # Check last letter
        word = word[:-1]
    if check(word[0]):  # Check first letter
        word = word[1:]
    return word


def count_words(sentence):
    word_arr = sentence.split(" ")
    word_map = {}
    for word in word_arr:
        word = check_punc_convert_lower(word)
        if word in word_map.keys():
            word_map[word] += 1
        else:
            word_map[word] = 1
    return word_map

