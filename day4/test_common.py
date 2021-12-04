import unittest

from common import (
    has_won,
    load_data,
    extract_bingo_boards,
    extract_drawn_numbers)


class TestSum(unittest.TestCase):
    def setUp(self):
        self.input = load_data('input.test')

    def test_has_won_horizontal(self):
        result = has_won([
            [1, 1, 1],
            [0, 0, 0],
            [1, 1, 0]
        ])

        self.assertTrue(result)

    def test_has_won_vertical(self):
        result = has_won([
            [0, 1, 1],
            [0, 1, 0],
            [1, 1, 0]
        ])

        self.assertTrue(result)

    def test_has_won_false(self):
        result = has_won([
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0]
        ])

        self.assertFalse(result)

    def test_extract_drawn_numbers(self):
        result = extract_drawn_numbers(self.input)

        self.assertEqual(result,
                         [7,
                          4,
                          9,
                          5,
                          11,
                          17,
                          23,
                          2,
                          0,
                          14,
                          21,
                          24,
                          10,
                          16,
                          13,
                          6,
                          15,
                          25,
                          12,
                          22,
                          18,
                          20,
                          8,
                          19,
                          3,
                          26,
                          1])

    def test_extract_bingo_boards(self):
        result = extract_bingo_boards(self.input)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[2], [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ])


if __name__ == "__main__":
    unittest.main()
