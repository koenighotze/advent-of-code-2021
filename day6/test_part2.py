import unittest

from part2 import part2


class TestSum(unittest.TestCase):
    def setUp(self):
        self.input = [3, 4, 3, 1, 2]

    def test_part1_18_days(self):
        number_of_lanternfish = part2(self.input, 18)

        self.assertEqual(number_of_lanternfish, 26)

    def test_part1(self):
        number_of_lanternfish = part2(self.input, 80)

        self.assertEqual(number_of_lanternfish, 5934)

    def test_part2(self):
        number_of_lanternfish = part2(self.input, 256)

        self.assertEqual(number_of_lanternfish, 26984457539)


if __name__ == "__main__":
    unittest.main()
