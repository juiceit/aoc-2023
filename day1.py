import re

spelled_out_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_value(digit):
    if digit in spelled_out_digits:
        return spelled_out_digits[digit]
    else:
        return int(digit)


with open("inputs/day1", "r") as f:
    lines = f.readlines()

# part 1
sum = 0
for line in lines:
    digits = re.findall("\d", line)
    sum += int(digits[0] + digits[-1])
print(sum)

# part 2
sum = 0
digit_regex = "(\d|one|two|three|four|five|six|seven|eight|nine)"

for line in lines:
    matches = re.search(digit_regex, line)
    if matches is not None:
        first_digit = matches[0]

    for i in range(len(line) - 1, -1, -1):
        matches = re.match(digit_regex, line[i:])
        if matches is not None:
            last_digit = matches[0]
            break

    sum += int(get_value(first_digit) * 10 + get_value(last_digit))

print(sum)
