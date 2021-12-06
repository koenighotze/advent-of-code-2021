import sys
from common import load_data


def part2(fish, number_of_days):
    fish_ages = [0] * 9
    for f in fish:
        fish_ages[f] += 1

    for _ in range(number_of_days):
        fish_born = fish_ages[0]
        for i in range(1, 9):
            fish_ages[i - 1] = fish_ages[i]
        fish_ages[8] = fish_born
        fish_ages[6] += fish_born

    return sum(fish_ages)


if __name__ == "__main__":
    RESULT = part2(load_data(sys.argv[1]), 256)
    print(f"Result is: {RESULT}")
