import re
from tqdm import tqdm
import math


def parse_map_line(map_line):
    return [int(number) for number in map_line.split()]


def parse_map(map_string):
    map_lines = map_string.splitlines()
    return [parse_map_line(m) for m in map_lines]


def parse_seeds(seeds_line):
    seed_strings = seeds_line.split(":")[1].split()
    return [int(s) for s in seed_strings]


def parse_input():
    with open("inputs/day5", "r") as f:
        seeds_line = f.readline()
        lines = f.read()

    seeds = parse_seeds(seeds_line)
    map_strings = re.split("\n.* map:\n", lines)
    maps = [parse_map(m) for m in map_strings if m != "\n"]
    return (seeds, maps)


def find_mapped_index(index, maps):
    for m in maps:
        destination = m[0]
        source = m[1]
        range = m[2]
        if index >= source and index < source + range:
            diff = index - source
            return destination + diff
    return index


def find_location(seed, maps):
    index = seed
    for m in maps:
        index = find_mapped_index(index, m)
    return index


def solve_part1(seeds, maps):
    locations = [find_location(seed, maps) for seed in seeds]
    return sorted(locations)[0]


def pair_seeds(seeds):
    return [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]


def find_lowest_location(seed_pair, maps):
    seeds = range(seed_pair[0], seed_pair[0] + seed_pair[1])
    lowest_location = math.inf
    for seed in tqdm(seeds):
        location = find_location(seed, maps)
        lowest_location = min(location, lowest_location)
    return lowest_location


def solve_part2(seeds, maps):
    seed_pairs = pair_seeds(seeds)
    lowest_location = math.inf
    for seed_pair in tqdm(seed_pairs):
        location = find_lowest_location(seed_pair, maps)
        lowest_location = min(location, lowest_location)
        print(lowest_location)
    return lowest_location


if __name__ == "__main__":
    seeds, maps = parse_input()
    print(solve_part1(seeds, maps))
    print(solve_part2(seeds, maps))
