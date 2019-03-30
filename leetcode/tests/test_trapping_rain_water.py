import unittest
from leetcode.trapping_rain_water import trap_rain_water


# python -m leetcode.tests.test_trapping_rain_water

class TestTrappingRainWater(unittest.TestCase):

    def test_1(self):
        arr = [1,2,4,0,6,8,5]
        self.assertEqual(trap_rain_water(arr),4)

    def test_2(self):
        arr = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(trap_rain_water(arr), 6)


if __name__ == "__main__":
    unittest.main()
