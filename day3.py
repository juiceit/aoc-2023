import re

with open("inputs/day3", "r") as f:
    lines = f.readlines()

symbol_pattern = "[^\d\.\s]"


def is_symbol_before(start, line):
    return start > 0 and re.search(symbol_pattern, line[start - 1])


def is_symbol_after(end, line):
    return end < len(line) and re.search(symbol_pattern, line[end])


def is_symbol_in_line(start, end, line):
    return re.search(
        symbol_pattern,
        line[start:end],
    )


def is_symbol_above(start, end, line_above_index):
    return line_above_index >= 0 and is_symbol_in_line(
        start, end, lines[line_above_index]
    )


def is_symbol_below(start, end, line_below_index):
    return line_below_index < len(lines) - 1 and is_symbol_in_line(
        start, end, lines[line_below_index]
    )


# part 1
valid_numbers = []
for line_index, line in enumerate(lines):
    number_matches = re.finditer("\d+", line)
    for m in number_matches:
        start, end = m.span()
        number = m.group()
        before_pos = max(0, start - 1)
        after_pos = min(end + 1, len(line))

        if (
            is_symbol_before(start, line)
            or is_symbol_after(end, line)
            or is_symbol_above(before_pos, after_pos, line_index - 1)
            or is_symbol_below(before_pos, after_pos, line_index + 1)
        ):
            valid_numbers.append(int(number))

print(sum(valid_numbers))

# part 2
gears = []
for line in lines:
    line_gears = {}
    found_gears = re.findall("\*", line)
    last_index = 0
    for gear in found_gears:
        index = last_index + line[last_index:].index(gear)
        last_index = index + 1
        line_gears[index] = []
    gears.append(line_gears)

for line_index, line in enumerate(lines):
    numbers = re.findall("\d+", line)
    last_index = 0
    for number in numbers:
        start = last_index + line[last_index:].index(number)
        end = start + len(number)
        last_index = end

        if start > 0 and re.search("[\*]", line[start - 1]):
            gears[line_index][start - 1].append(number)
        if end < len(line) and re.search("[\*]", line[end]):
            gears[line_index][end].append(number)
        if line_index > 0:
            line_above = lines[line_index - 1][
                max(0, start - 1) : min(end + 1, len(line))
            ]
            gs = re.findall("[\*]", line_above)
            g_last_index = 0
            for g in gs:
                g_index = g_last_index + line_above[g_last_index:].index(g)
                g_last_index = g_index + 1
                gears[line_index - 1][max(0, start - 1) + g_index].append(number)
        if line_index < len(lines) - 1:
            line_below = lines[line_index + 1][
                max(0, start - 1) : min(end + 1, len(line))
            ]
            gs = re.findall("[\*]", line_below)
            g_last_index = 0
            for g in gs:
                g_index = g_last_index + line_below[g_last_index:].index(g)
                g_last_index = g_index + 1
                gears[line_index + 1][max(0, start - 1) + g_index].append(number)

gear_power = 0

for line_gears in gears:
    for key in line_gears:
        if len(line_gears[key]) == 2:
            gear_power += int(line_gears[key][0]) * int(line_gears[key][1])

print(gear_power)
