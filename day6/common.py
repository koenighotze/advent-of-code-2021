def load_data(file_name):
    with open(file=file_name, mode="r", encoding="UTF-8") as file:
        return list(map(lambda e: int(e), list(
            map(lambda line: line.strip().split(","), file.readlines()))[0]))
