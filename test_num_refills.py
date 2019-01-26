import unittest

from num_refills import min_refills_original as  min_refills

class TestNumRefills(unittest.TestCase):

    def test_1(self):
        res = min_refills([0,350,600,750,900],3,400)
        self.assertEqual(res,2)


    def test_2(self):
        res = min_refills([0,350,750,900],3,400)
        self.assertEqual(res,2)

    def test_3(self):
        res = min_refills([0,750,900],3,400)
        self.assertEqual(res,"impossible")

    def test_4(self):
        res = min_refills([0,400,750,900,1400],3,400)
        self.assertEqual(res, 3)


if __name__ == "__main__":
    unittest.main()