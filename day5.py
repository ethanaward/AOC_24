
rules_f = {}
rules_b = {}
printings = []

with open('input/test5.txt', 'r') as f:
    line = f.readline().strip()
    while '|' in line:
        vals = line.split('|')
        if vals[0] in rules_f:
            rules_f[vals[0]].append(vals[1])
        else:
            rules_f[vals[0]] = [vals[1]]
        if vals[1] in rules_b:
            rules_b[vals[1]].append(vals[0])
        else:
            rules_b[vals[1]] = [vals[0]]
        line = f.readline().strip()
    for line in f.readlines():
        printings.append(line.strip().split(','))

invalid_printings = []

def is_valid(idx, value, forward_rules, backwards_rules, value_list):
    if value in forward_rules:
        for f_value in forward_rules[value]:
            if f_value in value_list[:idx]:
                return False
    if value in backwards_rules:
        for b_value in backwards_rules[value]:
            if b_value in value_list[idx + 1:]:
                return False
    return True


# Part 1
middle_total = 0
for printing in printings:
    is_printing_valid = True
    for idx, value in enumerate(printing):
        is_printing_valid = is_valid(idx, value, rules_f, rules_b, printing)
        if not is_printing_valid:
            break
    if is_printing_valid:
        middle_total += int(printing[int((len(printing) - 1) / 2)])
    else:
        invalid_printings.append(printing)
    is_printing_valid = True

print("The sum for part 1 is: {}".format(middle_total))

print(invalid_printings)

invalid_middle_total = 0
for invalid_printing in invalid_printings:
    new_list = []
    for value in invalid_printing:
        new_list.append(value)

    invalid_middle_total += int(new_list[int((len(new_list) - 1) / 2)])

