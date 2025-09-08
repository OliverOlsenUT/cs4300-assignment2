import copy

class Node():
    def __init__(self):
        self.map = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.prev_actions = []
        self.g = 0

    def transition(self, a):
        new_node = copy.deepcopy(self)
        a = a.lower()
        row, col = new_node.find_zero()

        if a == "up":
            new_node.map[row][col], new_node.map[row - 1][col] = new_node.map[row - 1][col], new_node.map[row][col]
        elif a == "down":
            new_node.map[row][col], new_node.map[row + 1][col] = new_node.map[row + 1][col], new_node.map[row][col]
        elif a == "left":
            new_node.map[row][col], new_node.map[row][col - 1] = new_node.map[row][col - 1], new_node.map[row][col]
        elif a == "right":
            new_node.map[row][col], new_node.map[row][col + 1] = new_node.map[row][col + 1], new_node.map[row][col]
        
        new_node.prev_actions.append(a)
        return new_node

    def find_zero(self):
        x = 0
        for a in self.map:
            y = 0
            for b in a:
                if b == 0:
                    return (x, y)
                y += 1
            x += 1
        raise Exception("Zero not found") 

    def actions(self):
        actions = ["up", "down", "left", "right"]
        row, col = self.find_zero()

        if row == 0:
            actions.remove("up")
        elif row == 2:
            actions.remove("down")
        if col == 0:
            actions.remove("left")
        elif col == 2:
            actions.remove("right")
        
        return actions

    def __str__(self):
        return str(self.map)

    def __eq__(self, other):
        return self.map == other.map

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.map))

GOAL = Node()
def goal_test(n):
    return n == GOAL
GOAL_POSITIONS = {tile: (r, c) for r, row in enumerate(GOAL.map) for c, tile in enumerate(row) if tile != 0}

def h0(node):
    return 0
def h1(node):
    return None # not yet implemented
def h2(node):
    distance = 0
    for r, row in enumerate(node.map):
        for c, tile in enumerate(row):
            if tile != 0:
                goal_r, goal_c = GOAL_POSITIONS[tile]
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance

