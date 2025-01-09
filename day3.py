import re
from functools import reduce

# Part 1
with open('input/input3.txt', 'r') as f:
    total = 0
    for line in f.readlines():
        matches = re.findall(r'mul\((\d+),(\d+)\)', line)
        line_total = reduce(lambda x, y: int(x[0]) * int(x[1]) + int(y[0]) * int(y[1]) if type(x) is tuple else x + int(y[0]) * int(y[1]), matches)
        total += line_total
    print(total)


def parse_memory(inst_matches: list, flag: bool) -> (int, bool):
    total = 0
    for match in inst_matches:
        if match[2]:
            flag = True
        elif match[3]:
            flag = False
        elif flag:
            total += int(match[0]) * int(match[1])
    return total, flag


# Part 2
with open('input/input3.txt', 'r') as f:
    full_regex = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")
    total = 0
    enabled = True
    for line in f.readlines():
        matches = re.findall(full_regex, line)
        (line_total, enabled) = parse_memory(matches, enabled)
        total += line_total
    print(total)








