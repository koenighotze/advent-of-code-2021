import sys
from common import load_data, dump


def low_point(x, y, input):
    candidate = input[x][y]
    above = x <= 0 or candidate < input[x - 1][y]
    below = x == len(input) - 1 or candidate < input[x + 1][y]
    left = y <= 0 or candidate < input[x][y - 1]
    right = y == len(input[0]) - 1 or candidate < input[x][y + 1]

    return above and below and left and right


def low_points(input):
    dump(input)
    print()
    candidates = []
    for row in range(len(input)):
        for col in range(len(input[0])):
            if low_point(row, col, input):
                candidates.append(input[row][col])
    return candidates


def parse(raw_input):
    return [[int(char) for char in line] for line in raw_input]


def risk_levels(input):
    return [i + 1 for i in input]


def part1(lines):
    return sum(risk_levels(low_points(parse(lines))))


if __name__ == "__main__":
    RESULT = part1(load_data(sys.argv[1]))
    print(f"Result is: {RESULT}")
