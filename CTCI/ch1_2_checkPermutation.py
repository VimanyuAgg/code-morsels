from collections import Counter
import unittest

# Space O(k) -> k is the number of unique characters in str1
# Time O(n) -> n is the length of the strings (have to be equal)
def check_permutation(str1, str2):
  if (not str1) or (not str2) or (len(str1) != len(str2)):
    return False
  counter = Counter(str1)
  for s in str2:
    if counter[s] == 0:
      return False
    counter[s] -= 1
  return True

class Test(unittest.TestCase):
  dataT = (
    ('abcd', 'bacd'),
    ('3563476', '7334566'),
    ('wef34f', 'wffe34'),
  )
  dataF = (
    ('abcd', 'd2cba'),
    ('2354', '1234'),
    ('dcw4f', 'dcw5f'),
  )

  def test_cp(self):
    # true check
    for test_strings in self.dataT:
      result = check_permutation(*test_strings)
      self.assertTrue(result)
    # false check
    for test_strings in self.dataF:
      result = check_permutation(*test_strings)
      self.assertFalse(result)


if __name__ == "__main__":
  unittest.main()