import sys
from common import load_data
from part1 import parse, low_point
from functools import reduce


def find_basin(x, y, input, current_basin):
    if [x, y] in current_basin:
        return

    current_basin.append([x, y])

    if x < len(input) - 1 and input[x + 1][y] != 9:
        find_basin(x + 1, y, input, current_basin)
    if x > 0 and input[x - 1][y] != 9:
        find_basin(x - 1, y, input, current_basin)
    if y < len(input[0]) - 1 and input[x][y + 1] != 9:
        find_basin(x, y + 1, input, current_basin)
    if y > 0 and input[x][y - 1] != 9:
        find_basin(x, y - 1, input, current_basin)

    return [input[i[0]][i[1]] for i in current_basin]


def low_points(input):
    candidates = []
    for row in range(len(input)):
        for col in range(len(input[0])):
            if low_point(row, col, input):
                candidates.append([row, col])
    return candidates


def part2(lines):
    input = parse(lines)

    basins = list(reversed(sorted(
        [find_basin(c[0], c[1], input, [])
            for c in low_points(input)], key=len)))

    largest = basins[:3]

    return reduce(lambda a, c: a * c, map(len, largest), 1)


if __name__ == "__main__":
    RESULT = part2(load_data(sys.argv[1]))
    print(f"Result is: {RESULT}")
