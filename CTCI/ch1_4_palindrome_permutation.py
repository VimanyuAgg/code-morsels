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

if __name__ == "__main__":
    unittest.main()