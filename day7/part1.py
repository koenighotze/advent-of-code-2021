import sys
from common import load_data
from statistics import median


def part1(positions):
    m = median(positions)
    oil_usage = 0

    for pos in positions:
        oil_usage += abs(m - pos)

    return dict(
        oil_spent=oil_usage,
        target_pos=m
    )


if __name__ == "__main__":
    RESULT = part1(list(map(int, load_data(sys.argv[1])[0].split(","))))
    print(f"Result is: {RESULT}")
