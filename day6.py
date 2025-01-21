import numpy as np


class Guard:
    direction = "u"
    x = 0
    y = 0
    turns = {}

    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = int(x)
        self.y = int(y)
        self.turns = {}

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
        if (self.x, self.y) in self.turns:
            self.turns[(self.x, self.y)] += 1
        else:
            self.turns[(self.x, self.y)] = 1
        match self.direction:
            case "u": self.direction = "r"
            case "r": self.direction = "d"
            case "d": self.direction = "l"
            case "l": self.direction = "u"

    # This is an inefficient way to determine this, but something cleaner wasn't coming to mind.
    def is_looped(self):
        return len([x for x in self.turns if self.turns[x] > 20]) > 0


np_arr = np.loadtxt('input/input6.txt', dtype=np.str_, comments='%')
np_matrix = np.array([list(s) for s in np_arr])

# Part 1
starting_point = np.where(np_matrix == '^')

guard = Guard('u', starting_point[0], starting_point[1])
visited_pos = []
while 0 <= guard.x < len(np_matrix) and 0 <= guard.y < len(np_matrix):
    if np_matrix[(guard.x, guard.y)] == '#':
        guard.backward()
        guard.turn()
    visited_pos.append((guard.x, guard.y))
    guard.forward()
print("The guard has visited {} positions.".format(len(set(visited_pos))))


# Part 2
def test_position(layout, new_guard):
    while 0 <= new_guard.x < len(layout) and 0 <= new_guard.y < len(layout) and not new_guard.is_looped():
        if layout[(new_guard.x, new_guard.y)] == '#':
            new_guard.backward()
            new_guard.turn()
        visited_pos.append((new_guard.x, new_guard.y))
        new_guard.forward()
    return new_guard.is_looped()


possible_blocks = 0
# You only need to check putting blocks in places the guard visits, since that's the only way the
# path of the guard will change.
for position in set(visited_pos):
    new_matrix = np_matrix.copy()
    new_matrix[position] = '#'
    guard = Guard('u', starting_point[0], starting_point[1])
    looped = test_position(new_matrix, guard)
    if looped:
        # print(new_matrix)
        possible_blocks += 1


print("There are {} possible locations to loop the guard.".format(possible_blocks))