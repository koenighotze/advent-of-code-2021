import sys
from common import load_data, calc_score, parse_row


def mark(field, c1, r1, c2, r2):
    if r1 == r2:
        start = c1 if c1 < c2 else c2
        end = c2 if c1 < c2 else c1

        for c in range(start, end + 1):
            field[r1][c] += 1

    if c1 == c2:
        start = r1 if r1 < r2 else r2
        end = r2 if r1 < r2 else r1

        for r in range(start, end + 1):
            field[r][c1] += 1


def build_field(input, field_size):
    field = [[0 for col in range(field_size)] for row in range(field_size)]
    for row in input:
        print(f"Row: {row}")
        [c1, r1, c2, r2] = parse_row(row)

        if c1 != c2 and r1 != r2:
            print("Skipping, not a horizontal or vertical line")
            continue

        mark(field, c1, r1, c2, r2)
    # dump(field)
    return field


def part1(input, field_size):
    return calc_score(build_field(input, field_size))


if __name__ == "__main__":
    RESULT = part1(load_data(sys.argv[1]), 1000)
    print(f"Result is: {RESULT}")
