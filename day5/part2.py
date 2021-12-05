import sys
from functools import reduce
from common import load_data, parse_row


def calc_score(matrix):
    rows = [list(filter(lambda e: e >= 2, row)) for row in matrix]
    return reduce(lambda a, e: a + len(e), rows, 0)


def mark(field, c1, r1, c2, r2):
    x = 0
    y = 0
    if c2 > c1:
        x = 1
    elif c2 < c1:
        x = -1

    if r2 > r1:
        y = 1
    elif r2 < r1:
        y = -1

    c = c1
    r = r1

    field[r][c] += 1
    while c != c2 or r != r2:
        c += x
        r += y
        field[r][c] += 1


def build_field(input, dim):
    field = [[0 for col in range(dim)] for row in range(dim)]
    for row in input:
        print(f"Row: {row}")
        [c1, r1, c2, r2] = parse_row(row)

        if c1 == c2:
            print("\tVertical")
        elif r1 == r2:
            print("\tHorizontal")
        elif abs(r2 - r1) == abs(c2 - c1):
            print("\tDiagonal")
        else:
            print("\tSkipping, not usable")
            continue

        mark(field, c1, r1, c2, r2)
    return field


def part2(input, dim):
    return calc_score(build_field(input, dim))


if __name__ == "__main__":
    RESULT = part2(load_data(sys.argv[1]), 1000)
    print(f"Result is: {RESULT}")
