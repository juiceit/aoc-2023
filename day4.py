import numpy as np


def parse_input():
    def string_to_set(numbers):
        return set(numbers.split())

    with open("inputs/day4", "r") as f:
        lines = f.readlines()

    card_wins = []

    for line in lines:
        _, numbers = line.split(":")
        winning_numbers, my_numbers = map(string_to_set, numbers.split("|"))
        my_winning_numbers = winning_numbers.intersection(my_numbers)
        card_wins.append(len(my_winning_numbers))

    return card_wins


def solve_part1(card_wins):
    def calc_points(wins):
        if wins > 0:
            return pow(2, wins - 1)
        else:
            return 0

    return sum(map(calc_points, card_wins))


def solve_part2(card_wins):
    card_copies = np.ones(len(card_wins), dtype=int)

    for i, wins in enumerate(card_wins):
        card_copies[i + 1 : i + 1 + wins] += card_copies[i]

    return sum(card_copies)


if __name__ == "__main__":
    card_wins = parse_input()
    print(solve_part1(card_wins))
    print(solve_part2(card_wins))
