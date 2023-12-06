import math


def parse_input():
    with open("inputs/day6", "r") as f:
        lines = f.readlines()
    return lines


def calc_ways_to_win(time, distance):
    ways = 0
    for button_time in range(0, time):
        speed = button_time
        travel_time = time - button_time
        travel_distance = travel_time * speed
        if travel_distance > distance:
            ways += 1
    return ways


def solve_part1(lines):
    times = [int(time) for time in lines[0].split(":")[1].split()]
    distances = [int(distance) for distance in lines[1].split(":")[1].split()]
    races = list(zip(times, distances))

    ways = []
    for race in races:
        time, distance = race
        way_to_win_race = calc_ways_to_win(time, distance)
        ways.append(way_to_win_race)
    return math.prod(ways)


def solve_part2(lines):
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))
    return calc_ways_to_win(time, distance)


if __name__ == "__main__":
    lines = parse_input()
    print(solve_part1(lines))
    print(solve_part2(lines))
