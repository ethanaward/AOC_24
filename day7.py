from itertools import product
equations = []

with open('input/input7.txt', 'r') as f:
    for line in f.readlines():
        parts = line.strip().split(':')
        equations.append((parts[0], parts[1].split(' ')[1:]))


# Part 1
correct_equation_total = 0
for result, operands in equations:
    current_total = int(operands[0])
    for permutation in product('am', repeat=len(operands) - 1):
        for idx, value in enumerate(list(permutation)):
            operand_val = int(operands[idx + 1])
            current_total = current_total + operand_val if value == 'a' else current_total * operand_val
        if current_total == int(result):
            correct_equation_total += int(result)
            break
        current_total = int(operands[0])

print('The total of the correct equations is {}.'.format(correct_equation_total))


# Part 2
# Could be combined as one but cleaner to separate
correct_concat_total = 0
for result, operands in equations:
    current_total = int(operands[0])
    for permutation in product('amc', repeat=len(operands) - 1):
        for idx, value in enumerate(list(permutation)):
            operand_val = int(operands[idx + 1])
            match value:
                case 'a': current_total += operand_val
                case 'm': current_total *= operand_val
                case 'c': current_total = int(str(current_total) + str(operand_val))
        if current_total == int(result):
            correct_concat_total += int(result)
            break
        current_total = int(operands[0])

print('The total of the correct equations with concat as an option is {}.'.format(correct_concat_total))
