import sys
from common import load_data


def simulate_day(fish_list):
    result = []
    new_fish = 0

    for fish in fish_list:
        if fish == 0:
            result.append(6)
            new_fish += 1
        else:
            result.append(fish - 1)

    return result + [8] * new_fish


def part1(fish, number_of_days):
    for day in range(number_of_days):
        fish = simulate_day(fish)
    return len(fish)


if __name__ == "__main__":
    RESULT = part1(load_data(sys.argv[1]), 80)
    print(f"Result is: {RESULT}")
