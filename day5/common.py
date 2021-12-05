from functools import reduce
import re


def create_checkboard(board):
    return [[0 for col in range(len(board[0]))] for row in range(len(board))]


def dump(matrix):
    for row in matrix:
        print(*row, sep=",")


def calc_score(matrix):
    rows = [list(filter(lambda e: e >= 2, row)) for row in matrix]
    return reduce(lambda a, e: a + len(e), rows, 0)


def load_data(file_name):
    with open(file=file_name, mode="r", encoding="UTF-8") as file:
        return list(map(lambda line: line.strip(), file.readlines()))


def parse_row(line):
    return list(map(int, filter(None,
                re.split(r'^(\d+),(\d+)\s+->\s+(\d+),(\d+)$', line))))
