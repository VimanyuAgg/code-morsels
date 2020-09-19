import unittest

'''
bale, bal
'''

# Space O(1)
# Time O(n)
# CTCI code repo has a more readable solution but with some duplication (same algorithm)
# https://github.com/VimanyuAgg/CtCI-6th-Edition-Python/blob/master/Chapter1/5_One%20Away/OneAway.py
# CTCI solution also added below
def one_away(str1, str2):
    p1, p2 = 0, 0
    diff_flag = False

    if (str1 is None) or (str2 is None) or (abs(len(str1) - len(str2)) > 1):
        return False

    while p1 < len(str1) and p2 < len(str2):
        if str1[p1] == str2[p2]:
            p1 += 1
            p2 += 1
        else:
            if diff_flag:
                return False

            diff_flag = True
            if len(str1) == len(str2):
                # It is a replacement case
                p1 += 1
                p2 += 1
            elif len(str1) > len(str2):
                p1 += 1
            else:
                p2 += 1
    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]


def test_one_away(self):
    for [test_s1, test_s2, expected] in self.data:
        actual = one_away(test_s1, test_s2)
        print(test_s1)
        self.assertEqual(actual, expected)


def one_away_ctci(s1, s2):
    '''Check if a string can converted to another string with a single edit'''
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    return False


def one_edit_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

if __name__ == "__main__":
    unittest.main()
