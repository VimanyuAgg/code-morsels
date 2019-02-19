import unittest


def find_factorial_zeroes_original(n):
    '''Counts trailing zeroes in n!'''
    power = 1
    res = 0
    if n < 0:
        return 0
    if n == 0:
        return 1
    while (n/(5**power) != 0):
        res += n//(5**power)
        power += 1
    return res


class TestFactorialTrailingZeroes(unittest.TestCase):

    def test1(self):
        self.assertEqual(find_factorial_zeroes_original(10),2)

    def test2(self):
        self.assertEqual(find_factorial_zeroes_original(15),3)

    def test3(self):
        self.assertEqual(find_factorial_zeroes_original(0),1)

    def test4(self):
        self.assertEqual(find_factorial_zeroes_original(26), 6)


if __name__ == "__main__":
    unittest.main()