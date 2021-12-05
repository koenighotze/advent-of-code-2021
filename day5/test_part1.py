import unittest

from part1 import part1, build_field
from common import load_data


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

    def test_build_field(self):
        field = build_field(self.input, 10)

        self.assertEqual(field, self.field)

    def test_part1(self):
        score = part1(self.input, 10)

        self.assertEqual(score, 5)


if __name__ == "__main__":
    unittest.main()
