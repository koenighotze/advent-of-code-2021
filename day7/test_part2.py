import unittest

from part2 import part2


class TestSum(unittest.TestCase):
    def test_part1(self):
        score = part2([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])

        self.assertEqual(score['oil_spent'], 168)
        self.assertEqual(score['target_pos'], 5)


if __name__ == "__main__":
    unittest.main()
