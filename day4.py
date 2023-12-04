import numpy as np

with open("inputs/day4", "r") as f:
    lines = f.readlines()


# part 1
def calc_points(wins):
    if wins > 0:
        return pow(2, wins - 1)
    else:
        return 0


card_wins = []

for line in lines:
    _, numbers = line.split(":")
    winning_numbers, my_numbers = map(lambda x: set(x.split()), numbers.split("|"))
    my_winning_numbers = winning_numbers.intersection(my_numbers)
    card_wins.append(len(my_winning_numbers))

print(sum(map(calc_points, card_wins)))


# part 2
card_copies = np.ones(len(lines), dtype=int)

for i, wins in enumerate(card_wins):
    card_copies[i + 1 : i + 1 + wins] += card_copies[i]

print(sum(card_copies))
