import numpy as np
from itertools import combinations
np_arr = np.loadtxt('input/input8.txt', dtype=np.str_)

np_matrix = np.array([list(s) for s in np_arr])


frequencies = np.unique(np_matrix[np.where(np_matrix != '.')])

antinodes = []

for frequency in frequencies:
    indices = np.argwhere(np_matrix == frequency)
    antenna_combinations = combinations(indices, 2)
    for combination in antenna_combinations:
        pt_1 = combination[0]
        pt_2 = combination[1]
        diff_x = abs(pt_2[0] - pt_1[0])
        diff_y = abs(pt_2[1] - pt_1[1])

        slope = (pt_2[1] - pt_1[1]) / (pt_2[0] - pt_1[0])
        intercept = pt_2[1] - (pt_2[0] * slope)

        first_pt = (int(max(pt_1[0], pt_2[0]) + diff_x), int(slope * (max(pt_1[0], pt_2[0]) + diff_x) + intercept))
        second_pt = (int(min(pt_1[0], pt_2[0]) - diff_x), int(slope * (min(pt_1[0], pt_2[0]) - diff_x) + intercept))

        if 0 <= first_pt[0] <= len(np_matrix) - 1 and 0 <= first_pt[1] <= len(np_matrix) - 1 and np_matrix[first_pt] == '.':
            antinodes.append(first_pt)
        if 0 <= second_pt[0] <= len(np_matrix) - 1 and 0 <= second_pt[1] <= len(np_matrix) - 1 and np_matrix[second_pt] == '.':
            antinodes.append(second_pt)

print("There are {} antinodes.".format(len(antinodes)))
