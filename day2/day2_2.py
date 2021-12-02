import sys


def day2(input):
    commands = {
        'forward': lambda v, c: [c[0] + v, c[1] + c[2] * v, c[2]],
        'down': lambda v, c: [c[0], c[1], c[2] + v],
        'up': lambda v, c: [c[0], c[1], c[2] - v],
    }

    current = [0, 0, 0]
    for [op, val] in [l.split() for l in input]:
        current = commands[op](int(val), current)
    return dict(H=current[0], D=current[1])


def load_data(file_name):
    with open(file=file_name, mode="r", encoding="UTF-8") as file:
        return list(map(lambda l: l.strip(), file.readlines()))


if __name__ == "__main__":
    RESULT = day2(load_data(sys.argv[1]))
    print(f"Result {RESULT['H'] * RESULT['D']}")
