
rules_f = {}
rules_b = {}
printings = []

with open('input/input5.txt', 'r') as f:
    line = f.readline().strip()
    while '|' in line:
        vals = line.split('|')
        if vals[0] in rules_f:
            rules_f[vals[0]].add(vals[1])
        else:
            rules_f[vals[0]] = {vals[1]}
        if vals[1] in rules_b:
            rules_b[vals[1]].add(vals[0])
        else:
            rules_b[vals[1]] = {vals[0]}
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

# Part 2
invalid_middle_total = 0
for invalid_printing in invalid_printings:
    new_list = []
    # Since we ignore all rules without numbers in this list, recreate our
    # forwards and backwards rules for this printing
    new_f = {}
    new_b = {}
    for value in invalid_printing:
        if value in rules_f:
            cur_value = [x for x in rules_f[value] if x in invalid_printing]
            new_f[value] = cur_value
    for key, value in new_f.items():
        for f_value in value:
            if f_value in new_b:
                new_b[f_value].append(key)
            else:
                new_b[f_value] = [key]
    # Now that we have the new backwards rules, we note that they define the correct order
    # for this printing by looking at the lengths of how many rules refer to them.
    rules_sorted = sorted(new_b, key=lambda key: len(new_b[key]))
    correct_order = list(new_b[rules_sorted[0]]) + rules_sorted

    invalid_middle_total += int(correct_order[int((len(correct_order) - 1) / 2)])

print("The sum for part 2 is {}".format(invalid_middle_total))
