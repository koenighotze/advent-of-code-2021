import unittest

from part1 import part1


class TestSum(unittest.TestCase):
    def setUp(self):
        self.input = [3, 4, 3, 1, 2]

    def test_part1_18_days(self):
        number_of_lanternfish = part1(self.input, 18)

        self.assertEqual(number_of_lanternfish, 26)

    def test_part1(self):
        number_of_lanternfish = part1(self.input, 80)

        self.assertEqual(number_of_lanternfish, 5934)


if __name__ == "__main__":
    unittest.main()
