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
def add_copies(cards, index, number_of_wins, number_of_copies):
    for i in range(index + 1, index + 1 + number_of_wins):
        if i < len(card_wins):
            cards[i] += number_of_copies


cards = [1] * len(card_wins)

for index, wins in enumerate(card_wins):
    add_copies(cards, index, wins, cards[index])

print(sum(cards))
