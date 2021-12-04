import unittest

from part1 import part1, determine_winning_board
from common import load_data, extract_bingo_boards, extract_drawn_numbers

class TestSum(unittest.TestCase):
    def setUp(self):
        self.input = load_data('input.test')

    def test_determine_winning_board(self):
        boards = extract_bingo_boards(self.input)
        numbers = extract_drawn_numbers(self.input)

        winner = determine_winning_board(boards, numbers)

        self.assertEqual(winner['board'], [
            [14, 21, 17, 24,  4],
            [10, 16, 15,  9, 19],
            [18,  8, 23, 26, 20],
            [22, 11, 13,  6,  5],
            [2,  0, 12,  3,  7],
        ])

        self.assertEqual(winner['number'], 24)

    def test_part1(self):
        score = part1(self.input)
        
        self.assertEqual(score, 4512)        


if __name__ == "__main__":
    unittest.main()