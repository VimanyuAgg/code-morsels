def is_palindrome_permutation(s):
    '''
    Checks if the given string is a permutation of a palindrome
    :param s: str
    :return: Bool
    '''
    if not s:
        return True

    bit_vector = 0
    for c in s:
        if c == " ":
            continue
        ord_c = ord(c.lower())  # Doesn't error out on spaces or numeric characters encoded in string
        bit_vector = bit_vector ^ (1 << ord_c)

    return bit_vector & (bit_vector - 1) == 0