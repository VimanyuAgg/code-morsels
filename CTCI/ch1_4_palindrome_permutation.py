import unittest

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

    # Python uses two's complement for bitwise signed integer representation so there's no negative zero
    # https://stackoverflow.com/questions/46044936/bitwise-and-between-negative-and-positive-numbers
    return bit_vector & (bit_vector - 1) == 0


from collections import Counter

def is_palindrome_permutation_2(s):
    if not s:
        return False
    s = s.replace(' ', '')
    s = s.lower()

    counter = Counter(s)
    is_even = len(s) % 2 == 0
    odd_check = False
    for k, v in counter.items():
        if is_even and (v % 2 != 0):
            return False
        if (not is_even) and (v % 2 != 0):
            if not odd_check:
                odd_check = True
                continue
            return False

    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = is_palindrome_permutation(test_string)
            self.assertEqual(actual, expected)
            actual = is_palindrome_permutation_2(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()