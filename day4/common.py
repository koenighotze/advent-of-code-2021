import re
from functools import reduce


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def horizontal_win(checks):
    res = [reduce(lambda a, b: a and b, row) for row in checks]
    return reduce(lambda a, b: a or b, res)


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
        print(*row, sep=",")
        print()


def extract_drawn_numbers(input):
    return [int(i) for i in input[0].split(',')]


def extract_bingo_boards(input):
    start = 2
    boards = []
    while start <= len(input) - 5:
        board = input[start:start + 5]
        boards.append([list(map(int, re.split(' +', row))) for row in board])
        print(*board, sep="\n")
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


def load_data(file_name):
    with open(file=file_name, mode="r", encoding="UTF-8") as file:
        return list(map(lambda line: line.strip(), file.readlines()))
