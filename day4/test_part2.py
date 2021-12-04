import unittest

from part2 import part2, determine_last_winning_board
from common import load_data, extract_bingo_boards, extract_drawn_numbers

class TestSum(unittest.TestCase):
    def setUp(self):
        self.input = load_data('input.test')

    def test_determine_last_winning_board(self):
        boards = extract_bingo_boards(self.input)
        numbers = extract_drawn_numbers(self.input)

        winner = determine_last_winning_board(boards, numbers)

        self.assertEqual(winner['board'], [
            [3, 15,  0,  2, 22],
            [9, 18, 13, 17,  5],
            [19,  8,  7, 25, 23],
            [20, 11, 10, 24,  4],
            [14, 21, 16, 12,  6]       
        ])

        self.assertEqual(winner['number'], 13)


    def test_part2(self):
        score = part2(self.input)
        
        self.assertEqual(score, 1924)        


if __name__ == "__main__":
    unittest.main()