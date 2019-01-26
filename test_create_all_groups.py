import unittest
from create_all_groups import combinations as group_n


class TestCreateAllGroups(unittest.TestCase):


    # def assertIterableEqual(self, iterable1, iterable2):
    #     self.assertEqual(set(iterable1), set(iterable2))
    #
    # def test_create_groups_1(self):
    #     group_of_ones = group_n([1,2,3],1)
    #     print(set(group_of_ones))
    #     # for groups in group_of_ones:
    #     #     for group in groups:
    #     #         print(group)
    #     # # self.assertIterableEqual(group_of_ones, {{1},{2},{3}})
    #
    def test_create_groups_2(self):
        group_of_twos = group_n([1,2,3],2)
        print(set(group_of_twos))
        # self.assertEqual(group_of_ones, {{1,2},{1,3},{2,3}})

    # def test_string(self):
    #     combination_string = group_n('ABCD', 2)
    #     print(list(combination_string))


if __name__ == "__main__":
        unittest.main()