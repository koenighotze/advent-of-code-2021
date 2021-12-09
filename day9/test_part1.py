import unittest

from part1 import part1, low_points, parse, risk_levels


class TestSum(unittest.TestCase):
    def setUp(self):
        self.input = [
            "2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678"
        ]
        self.parsed_input = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
        ]

    def test_parse(self):
        result = parse(self.input)

        self.assertEqual(result, self.parsed_input)

    def test_low_points(self):
        result = low_points(self.parsed_input)

        self.assertEqual(result, [1, 0, 5, 5])

    def test_risk_levels(self):
        result = risk_levels([1, 0, 5, 5])

        self.assertEqual(result, [2, 1, 6, 6])

    def test_part1(self):
        result = part1(self.input)

        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
