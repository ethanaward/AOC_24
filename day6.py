import numpy as np


class Guard:
    direction = "u"
    x = 0
    y = 0

    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y

    def forward(self):
        match self.direction:
            case "u": self.x -= 1
            case "r": self.y += 1
            case "d": self.x += 1
            case "l": self.y -= 1

    def backward(self):
        match self.direction:
            case "u": self.x += 1
            case "r": self.y -= 1
            case "d": self.x -= 1
            case "l": self.y += 1

    def turn(self):
        match self.direction:
            case "u": self.direction = "r"
            case "r": self.direction = "d"
            case "d": self.direction = "l"
            case "l": self.direction = "u"


np_arr = np.loadtxt('input/input6.txt', dtype=np.str_, comments='%')
np_matrix = np.array([list(s) for s in np_arr])

# Part 1
starting_point = np.where(np_matrix == '^')

guard = Guard('u', starting_point[0], starting_point[1])
visited_pos = []
# visited_pos = np.full_like(np_matrix, '-', dtype=np.str_)
while 0 <= guard.x < len(np_matrix) and 0 <= guard.y < len(np_matrix):
    # visited_pos[guard.x, guard.y] = 'X'
    if np_matrix[(guard.x, guard.y)] == '#':
        # visited_pos[(guard.x, guard.y)] = '-'
        guard.backward()
        guard.turn()
    visited_pos.append((guard.x[0], guard.y[0]))
    guard.forward()
print("The guard has visited {} positions.".format(len(set(visited_pos))))

