def load_data(file_name):
    with open(file=file_name, mode="r", encoding="UTF-8") as file:
        return list(map(lambda line: line.strip(), file.readlines()))


def dump(board):
    for row in board:
        print(*row, sep=",")
