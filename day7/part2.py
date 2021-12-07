import sys
from common import load_data


def part2(positions):
    min_oil_usage = 9999999999
    min_pos = 0
    for target_pos in range(min(positions), max(positions)):
        cur_oil_usage = 0
        for pos in positions:
            oil_needed = sum(range(abs(target_pos - pos) + 1))
            cur_oil_usage += oil_needed
            if cur_oil_usage > min_oil_usage:
                break
        if cur_oil_usage < min_oil_usage:
            min_oil_usage = cur_oil_usage
            min_pos = target_pos

    return dict(
        oil_spent=min_oil_usage,
        target_pos=min_pos
    )


if __name__ == "__main__":
    RESULT = part2(list(map(int, load_data(sys.argv[1])[0].split(","))))
    print(f"Result is: {RESULT}")
