import re

with open("inputs/day3", "r") as f:
    lines = f.readlines()


def is_pattern_before(pattern, start, line):
    return start > 0 and re.search(pattern, line[start - 1])


def is_pattern_after(pattern, end, line):
    return end < len(line) and re.search(pattern, line[end])


def is_pattern_in_line(pattern, start, end, line):
    return re.search(
        pattern,
        line[start:end],
    )


def is_pattern_above(pattern, start, end, line_above_index):
    return line_above_index >= 0 and is_pattern_in_line(
        pattern, start, end, lines[line_above_index]
    )


def is_pattern_below(pattern, start, end, line_below_index):
    return line_below_index < len(lines) - 1 and is_pattern_in_line(
        pattern, start, end, lines[line_below_index]
    )


# part 1
valid_numbers = []
symbol_pattern = "[^\d\.\s]"

for line_index, line in enumerate(lines):
    number_matches = re.finditer("\d+", line)
    for m in number_matches:
        start, end = m.span()
        number = m.group()
        before_pos = max(0, start - 1)
        after_pos = min(end + 1, len(line))

        if (
            is_pattern_before(symbol_pattern, start, line)
            or is_pattern_after(symbol_pattern, end, line)
            or is_pattern_above(symbol_pattern, before_pos, after_pos, line_index - 1)
            or is_pattern_below(symbol_pattern, before_pos, after_pos, line_index + 1)
        ):
            valid_numbers.append(int(number))

print(sum(valid_numbers))

# part 2
gears = {}


def add_number_to_gear(x, y, number):
    if x not in gears:
        gears[x] = {}
    if y in gears[x]:
        gears[x][y].append(number)
    else:
        gears[x][y] = [number]


for line_index, line in enumerate(lines):
    number_matches = re.finditer("\d+", line)
    for m in number_matches:
        start, end = m.span()
        number = int(m.group())
        before_pos = max(0, start - 1)
        after_pos = min(end + 1, len(line))

        if is_pattern_before("\*", start, line):
            add_number_to_gear(line_index, start - 1, number)
        if is_pattern_after("\*", end, line):
            add_number_to_gear(line_index, end, number)
        if line_index > 0:
            line_above = lines[line_index - 1][before_pos:after_pos]
            gear_matches = re.finditer("\*", line_above)
            for gm in gear_matches:
                add_number_to_gear(line_index - 1, before_pos + gm.start(), number)
        if line_index < len(lines) - 1:
            line_below = lines[line_index + 1][before_pos:after_pos]
            gear_matches = re.finditer("\*", line_below)
            for gm in gear_matches:
                add_number_to_gear(line_index + 1, before_pos + gm.start(), number)

sum_gear_ratios = 0

for x in gears:
    for y in gears[x]:
        if len(gears[x][y]) == 2:
            sum_gear_ratios += gears[x][y][0] * gears[x][y][1]

print(sum_gear_ratios)
