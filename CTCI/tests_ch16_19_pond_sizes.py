import unittest
from CTCI.ch16_19_pond_sizes import pond_sizes

class TestPondSizes(unittest.TestCase):

    def test1(self):
        earth = [[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]
        self.assertEqual(pond_sizes(earth),[2,4,1])


if __name__ == "__main__":
    unittest.main()

