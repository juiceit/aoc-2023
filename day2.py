max_red = 12
max_green = 13
max_blue = 14


def parse_input():
    with open("inputs/day2", "r") as f:
        lines = f.readlines()

    result = []
    for line in lines:
        _, game = line.split(": ")
        hands = game.split("; ")
        current_game = []
        for hand in hands:
            cubes = hand.split(", ")
            colors = {}
            for cube in cubes:
                number, color = cube.split()
                colors[color] = int(number)
            current_game.append(colors)
        result.append(current_game)
    return result


def is_hand_valid(colors):
    if "red" in colors and colors["red"] > max_red:
        return False
    if "green" in colors and colors["green"] > max_green:
        return False
    if "blue" in colors and colors["blue"] > max_blue:
        return False
    return True


def is_game_valid(hands):
    return all(map(is_hand_valid, hands))


games = parse_input()

# part 1
valid_games = [i + 1 for i, game in enumerate(games) if is_game_valid(game)]
print(sum(valid_games))

# part 2
powers = []
for game in games:
    red = 0
    green = 0
    blue = 0
    for hand in game:
        if "red" in hand and hand["red"] > red:
            red = hand["red"]
        if "green" in hand and hand["green"] > green:
            green = hand["green"]
        if "blue" in hand and hand["blue"] > blue:
            blue = hand["blue"]
    powers.append(red * green * blue)

print(sum(powers))
