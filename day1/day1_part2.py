import sys


def day1(measures):
    window_size = 3
    window = lambda values, pos: values[pos : pos + window_size]

    number_of_increases = 0
    for i in range(len(measures) - window_size):
        if sum(window(measures, i + 1)) > sum(window(measures, i)):
            number_of_increases += 1

    return number_of_increases


def load_data(file_name):
    with open(file=file_name, mode="r", encoding="UTF-8") as file:
        return list(map(lambda l: int(l.strip()), file.readlines()))


if __name__ == "__main__":
    RESULT = day1(load_data(sys.argv[1]))
    print(f"Number of increases {RESULT}")
