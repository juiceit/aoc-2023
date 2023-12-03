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
gears = []
for line in lines:
    line_gears = {}
    for m in re.finditer("\*", line):
        line_gears[m.start()] = []
    gears.append(line_gears)

for line_index, line in enumerate(lines):
    number_matches = re.finditer("\d+", line)
    for m in number_matches:
        start, end = m.span()
        number = int(m.group())
        before_pos = max(0, start - 1)
        after_pos = min(end + 1, len(line))

        if is_pattern_before("\*", start, line):
            gears[line_index][start - 1].append(number)
        if is_pattern_after("\*", end, line):
            gears[line_index][end].append(number)
        if line_index > 0:
            line_above = lines[line_index - 1][before_pos:after_pos]
            gear_matches = re.finditer("\*", line_above)
            for gm in gear_matches:
                gears[line_index - 1][before_pos + gm.start()].append(number)
        if line_index < len(lines) - 1:
            line_below = lines[line_index + 1][before_pos:after_pos]
            gear_matches = re.finditer("\*", line_below)
            for gm in gear_matches:
                gears[line_index + 1][before_pos + gm.start()].append(number)

sum_gear_ratios = 0

for line_gears in gears:
    for key in line_gears:
        if len(line_gears[key]) == 2:
            sum_gear_ratios += line_gears[key][0] * line_gears[key][1]

print(sum_gear_ratios)
