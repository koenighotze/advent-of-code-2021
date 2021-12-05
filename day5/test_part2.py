import unittest

from part2 import part2, build_field
from common import load_data


class TestSum(unittest.TestCase):
    def setUp(self):
        self.input = load_data('input.test')
        self.field = [
            [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
            [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
            [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
            [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [2, 2, 2, 1, 1, 1, 0, 0, 0, 0]
        ]

    def test_build_field(self):
        field = build_field(self.input, 10)

        self.assertEqual(field, self.field)

    def test_part2(self):
        score = part2(self.input, 10)

        self.assertEqual(score, 12)


if __name__ == "__main__":
    unittest.main()
