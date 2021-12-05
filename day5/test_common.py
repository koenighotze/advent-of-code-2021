import unittest

from common import (
    load_data, calc_score)


class TestSum(unittest.TestCase):
    def setUp(self):
        self.input = load_data('input.test')
        self.field = [
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 1, 1, 1, 0, 0, 0, 0]
        ]

    def test_calc_score(self):
        result = calc_score(self.field)

        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
