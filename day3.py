import re

with open("inputs/day3", "r") as f:
    lines = f.readlines()

# part 1
valid_numbers = []
for line_index, line in enumerate(lines):
    numbers = re.findall("\d+", line)
    last_index = 0
    for number in numbers:
        start = last_index + line[last_index:].index(number)
        end = start + len(number)
        last_index = end

        if start > 0 and re.search("[^\d\.\s]", line[start - 1]):
            valid_numbers.append(int(number))
        elif end < len(line) and re.search("[^\d\.\s]", line[end]):
            valid_numbers.append(int(number))
        elif line_index > 0 and re.search(
            "[^\d\.\s]",
            lines[line_index - 1][max(0, start - 1) : min(end + 1, len(line))],
        ):
            valid_numbers.append(int(number))
        elif line_index < len(lines) - 1 and re.search(
            "[^\d\.\s]",
            lines[line_index + 1][max(0, start - 1) : min(end + 1, len(line))],
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
