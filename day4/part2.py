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


def determine_last_winning_board(boards, numbers):
    current_number_idx = 0
    was_already_winner = []
    checkboards = list(map(create_checkboard, boards))
    last_winner = None
    while current_number_idx < len(numbers):
        current_number = numbers[current_number_idx]
        print(f"Next number: {current_number}")

        for board_number in range(len(boards)):
            checkboards[board_number] = update_checkboard(
                checkboards[board_number],
                boards[board_number],
                current_number)
            if board_number not in was_already_winner and has_won(
                    checkboards[board_number]):
                was_already_winner.append(board_number)
                print(f"New winner found!!! Board number {board_number}")
                last_winner = dict(
                    board=boards[board_number],
                    number=current_number,
                    check=checkboards[board_number])
                if len(was_already_winner) == len(boards):
                    return last_winner

        current_number_idx += 1
    return last_winner


def part2(input):
    boards = extract_bingo_boards(input)
    numbers = extract_drawn_numbers(input)
    winner = determine_last_winning_board(boards, numbers)
    return calc_score(winner)


if __name__ == "__main__":
    RESULT = part2(load_data(sys.argv[1]))
    print(f"Result is: {RESULT}")
