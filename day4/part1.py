import sys
from common import (
    has_won,
    load_data,
    extract_bingo_boards,
    extract_drawn_numbers,
    create_checkboard,
    update_checkboard,
    calc_score
    )


def determine_winning_board(boards, numbers):
    current_number_idx = 0
    winner_found = False

    checkboards = list(map(create_checkboard, boards))
    while not winner_found and current_number_idx <= len(numbers):
        current_number = numbers[current_number_idx]
        print(f"Next number: {current_number}")
        # for b in checkboards:
        #     dump(b)

        for board_number in range(len(boards)):
            checkboards[board_number] = update_checkboard(
                                        checkboards[board_number],
                                        boards[board_number],
                                        current_number)
            if has_won(checkboards[board_number]):
                print(f"Winner found!!! Board number {board_number}")
                return dict(
                    board=boards[board_number],
                    number=current_number,
                    check=checkboards[board_number])

        current_number_idx += 1


def part1(input):
    boards = extract_bingo_boards(input)
    numbers = extract_drawn_numbers(input)
    winner = determine_winning_board(boards, numbers)
    return calc_score(winner)


if __name__ == "__main__":
    RESULT = part1(load_data(sys.argv[1]))
    print(f"Result is: {RESULT}")
