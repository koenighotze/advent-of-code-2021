import sys

WINDOW_SIZE = 3


def window(values, pos):
    return values[pos:pos + WINDOW_SIZE]


def day1(measures):
    number_of_increases = 0
    for i in range(len(measures) - WINDOW_SIZE):
        if sum(window(measures, i + 1)) > sum(window(measures, i)):
            number_of_increases += 1

    return number_of_increases


def load_data(file_name):
    with open(file=file_name, mode="r", encoding="UTF-8") as file:
        return list(map(lambda l: int(l.strip()), file.readlines()))


if __name__ == "__main__":
    RESULT = day1(load_data(sys.argv[1]))
    print(f"Number of increases {RESULT}")
