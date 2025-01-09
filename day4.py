import numpy as np
import re


np_arr = np.loadtxt('input/input4.txt', dtype=np.str_)

np_matrix = np.array([list(s) for s in np_arr])


# Part 1
def count_matches(match_string: str) -> int:
    matches = re.findall(r'(?=(SAMX))|(?=(XMAS))', match_string)
    return len(matches)


count = 0
for idx in range(0, len(np_matrix)):
    if idx == 0:
        count += count_matches(''.join(np_matrix.diagonal(idx)))
        count += count_matches(''.join(np.fliplr(np_matrix).diagonal(idx)))
    else:
        count += count_matches(''.join(np_matrix.diagonal(idx)))
        count += count_matches(''.join(np_matrix.diagonal(-idx)))
        count += count_matches(''.join(np.fliplr(np_matrix).diagonal(idx)))
        count += count_matches(''.join(np.fliplr(np_matrix).diagonal(-idx)))
    count += count_matches(''.join(np_matrix[:, idx]))
    count += count_matches(''.join(np_matrix[idx, :]))
print("Count for part 1: {}".format(count))


# Part 2
# Old approach using numpy search
def find_matches(match_string: str) -> list[int]:
    matches = re.finditer(r'(?=(SAM))|(?=(MAS))', match_string)
    indices = []
    for match in matches:
        indices.append(match.span()[0] + 1)
    return indices


def add_match(idx1, idx2, all_matches, mat):
    if mat[idx1, idx2] != 'A':
        print(idx1, idx2, mat[idx1, idx2])
    if idx1 < 0:
        idx1 = len(mat) + idx1 + 1
    if idx2 < 0:
        idx2 = len(mat) + idx2 + 1
    if (idx1, idx2) in a_indices:
        all_matches += (idx1, idx2)
    else:
        a_indices[(idx1, idx2)] = 1
    return False


a_indices = {}
xmas_matches = []
# There's gotta be a cleaner way to do this in numpy
for idx in range(0, len(np_matrix)):
    if idx == 0:
        matches = find_matches(''.join(np_matrix.diagonal(idx)))
        for match in matches:
            add_match(match, match, xmas_matches, np_matrix)
    else:
        matches = find_matches(''.join(np_matrix.diagonal(idx)))
        for match in matches:
            add_match(match, match + idx, xmas_matches, np_matrix)
        matches = find_matches(''.join(np_matrix.diagonal(-idx)))
        for match in matches:
            add_match(match + idx, match, xmas_matches, np_matrix)
        matches = find_matches(''.join(np.fliplr(np_matrix).diagonal(idx)))
        for match in matches:
            add_match(match, -(match + idx + 1), xmas_matches, np_matrix)
        matches = find_matches(''.join(np.fliplr(np_matrix).diagonal(-idx)))
        for match in matches:
            add_match(match + idx, -(match + 1), xmas_matches, np_matrix)

# New approach - find As and check their diagonals

print(np_matrix)
count = 0
with np.nditer(np_matrix, flags=['multi_index']) as it:
    for x in it:
        if x == 'A':
            index = it.multi_index
            if 0 < index[0] < len(np_matrix) - 1 and 0 < index[1] < len(np_matrix) - 1:
                upper_left = np_matrix[index[0] - 1][index[1] - 1]
                lower_left = np_matrix[index[0] + 1][index[1] - 1]
                upper_right = np_matrix[index[0] - 1][index[1] + 1]
                lower_right = np_matrix[index[0] + 1][index[1] + 1]
                if (upper_left == 'M' and lower_right == 'S') or (upper_left == 'S' and lower_right == 'M'):
                    if (upper_right == 'S' and lower_left == 'M') or (upper_right == 'M' and lower_left == 'S'):
                        count += 1
print(count)