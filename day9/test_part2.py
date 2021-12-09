import unittest

from part2 import part2, find_basin


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

    def test_basin_of(self):
        result = sorted(find_basin(0, 0, self.parsed_input, []))

        self.assertEqual(result, [1, 2, 3])

    def test_basin_of_second_case(self):
        result = sorted(find_basin(0, 9, self.parsed_input, []))

        expected = sorted([4, 3, 2, 1, 0, 4, 2, 1, 2])
        self.assertEqual(result, expected)

    def test_part2(self):
        result = part2(self.input)

        self.assertEqual(result, 1134)


if __name__ == "__main__":
    unittest.main()
