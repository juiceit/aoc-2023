with open("inputs/day4", "r") as f:
    lines = f.readlines()

# part 1
points = 0
for line in lines:
    _, numbers = line.split(":")
    winning_numbers, my_numbers = map(lambda x: x.split(), numbers.split("|"))

    matches = [
        winning_number
        for winning_number in winning_numbers
        if winning_number in my_numbers
    ]

    if len(matches) > 0:
        points += pow(2, len(matches) - 1)

print(points)


# part 2
def add_copies(cards, line_index, number_of_wins):
    for i in range(line_index + 1, line_index + number_of_wins + 1):
        if i < len(lines):
            cards[i] += 1


cards = [1] * len(lines)
for line_index, line in enumerate(lines):
    _, numbers = line.split(":")
    winning_numbers, my_numbers = map(lambda x: x.split(), numbers.split("|"))

    matches = [
        winning_number
        for winning_number in winning_numbers
        if winning_number in my_numbers
    ]

    for i in range(0, cards[line_index]):
        add_copies(cards, line_index, len(matches))

print(sum(cards))
