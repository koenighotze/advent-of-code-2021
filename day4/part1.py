import sys
import re
from functools import reduce

def transpose(matrix): 
    return list(map(list, zip(*matrix)))

def horizontal_win(checks):
    res = [reduce(lambda a,b: a and b, row) for row in checks]
    return reduce(lambda a,b: a or b, res)

def vertical_win(checks):
    return horizontal_win(transpose(checks))

def has_won(checks):
    return horizontal_win(checks) or vertical_win(checks)

def create_checkboard(board):
    return [[0 for col in range(len(board[0]))] for row in range(len(board))]

def update_checkboard(checkboard, board, number):
    updated_checkboard = checkboard[:]

    for r in range(len(board)):
        for c in range(len(board[0])):
            if number == board[r][c]:
                # print(f"Found number at row {r} column {c}")
                updated_checkboard[r][c] = 1
                break

    return updated_checkboard

def dump(board):
    for row in board:
        print(*row, sep = ",") 
        print()

def determine_winning_board(boards, numbers):
    current_number_idx = 0
    winner_found = False

    checkboards = list(map(create_checkboard, boards))
    while not winner_found and current_number_idx <= len(numbers):
        current_number = numbers[current_number_idx]
        print(f"Next number: {current_number}")
        # for b in checkboards:
        #     dump(b)

        for board_number in range(len(boards)):
            checkboards[board_number] = update_checkboard(checkboards[board_number], boards[board_number], current_number)
            if has_won(checkboards[board_number]):
                print(f"Winner found!!! Board number {board_number}")
                return dict(
                    board=boards[board_number], 
                    number=current_number,
                    check=checkboards[board_number])

        current_number_idx += 1


def extract_drawn_numbers(input):
    return [int(i) for i in input[0].split(',')]

def extract_bingo_boards(input):
    start = 2
    boards = []
    while start <= len(input) - 5:
        board = input[start:start+5]
        boards.append([list(map(int, re.split(' +', row))) for row in board])
        print(*board, sep = "\n")
        print("-----------")
        start += 6
    return boards

def sum(board, check):
    res = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            res += abs(board[r][c] * (check[r][c] - 1))
    return res
        
def calc_score(winner):
    result = sum(winner['board'], winner['check'])
    return result * winner['number']

def part1(input):
    boards = extract_bingo_boards(input)
    numbers = extract_drawn_numbers(input)
    winner = determine_winning_board(boards, numbers)
    return calc_score(winner)

def load_data(file_name):
    with open(file=file_name, mode="r", encoding="UTF-8") as file:
        return list(map(lambda line: line.strip(), file.readlines()))


if __name__ == "__main__":
    RESULT = part1(load_data(sys.argv[1]))
    print(f"Result is: {RESULT}")