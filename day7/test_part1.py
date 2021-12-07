import unittest

from part1 import part1


class TestSum(unittest.TestCase):
    def test_part1(self):
        score = part1([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])

        self.assertEqual(score['oil_spent'], 37)
        self.assertEqual(score['target_pos'], 2)


if __name__ == "__main__":
    unittest.main()
