# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.#
# Find the sum of all the multiples of 3 or 5 below 1000.

import unittest

def find_smaller_larger(num1,num2):
    if num1 > num2:
        return num2, num1
    else:
        return num1, num2

def sum_multiple_under_n(num1,num2,limit):

    smaller_num, larger_num = find_smaller_larger(num1,num2)
    curr = smaller_num

    sum = 0
    while curr < limit:
        if (curr % larger_num == 0) or (curr % smaller_num == 0):
            sum += curr

        curr += 1

    return sum


class TestEulerProblem1(unittest.TestCase):

    def test1(self):
        self.assertEqual(sum_multiple_under_n(3,5,10),23)

    def answer(self):
        print(sum_multiple_under_n(3,5,1000))


if __name__ == "__main__":
    unittest.main()