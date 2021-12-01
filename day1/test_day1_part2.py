import unittest

from day1_part2 import day1

class TestSum(unittest.TestCase):
    def test_day1(self):
        measures = [ 199, 200, 208, 210, 200, 207, 240, 269, 260, 263 ]

        result = day1(measures)

        self.assertEqual(result, 5)

    def test_empty_list_results_in_zero(self):
        result = day1([])
        
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
