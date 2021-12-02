import unittest

from day2 import day2


class TestSum(unittest.TestCase):
    def test_day2(self):
        input = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
        ]

        result = day2(input)

        self.assertEqual(result['H'], 15)
        self.assertEqual(result['D'], 10)


if __name__ == "__main__":
    unittest.main()
