

left = []
right = []

with open('input/input.txt', 'r') as f:
    for line in f.readlines():
        vals = line.split()
        left.append(int(vals[0]))
        right.append(int(vals[1]))

print(sum(map(lambda x,y: abs(x - y), sorted(left), sorted(right))))


left_set = set(left)
right_set = set(right)
considerations = left_set.intersection(right_set)

val = 0
for poss_num in considerations:
    right_ind = [x for x, y in enumerate(right) if y == poss_num]
    left_ind = [x for x, y in enumerate(left) if y == poss_num]
    val += len(right_ind) * len(left_ind) * poss_num
print(val)

