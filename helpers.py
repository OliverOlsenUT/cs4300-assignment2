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
    misplaced = 0
    for r, row in enumerate(node.map):
        for c, tile in enumerate(row):
            if tile != 0 and tile != GOAL.map[r][c]:
                misplaced += 1
    return misplaced
def h2(node):
    distance = 0
    for r, row in enumerate(node.map):
        for c, tile in enumerate(row):
            if tile != 0:
                goal_r, goal_c = GOAL_POSITIONS[tile]
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance

class Result():
    def __init__(self):
        self.nodes_generated = 0
        self.nodes_expanded = 0
        self.maximum_frontier_size = 0
        self.solution_depth = 0
        self.solution_cost = 0
        self.prev_actions = []
        self.type = ""
    def __str__(self):
        return f"Result Type: {self.type} \
                \nNodes Generated: {self.nodes_generated} | Nodes Expanded: {self.nodes_expanded} | Max Frontier Size: {self.maximum_frontier_size} \
                \nSolution Depth: {self.solution_depth} | Solution Cost: {self.solution_cost} | Solution Path: {self.prev_actions}"

def print_solution_path(inital_state, actions_to_sol):
    s = copy.deepcopy(inital_state)
    print("Initial State:", s)
    print("Solution Steps:")
    for x in actions_to_sol:
        s = s.transition(x)
        print("Moved", x, "New state:", s)
    print("Reached goal state.")

TEST_MAPS = [
    [[1, 2, 3], [4, 5, 6], [0, 7, 8]],
    [[1, 2, 3], [4, 5, 0], [7, 8, 6]],
    [[1, 2, 3], [4, 8, 5], [7, 0, 6]],
    [[1, 2, 3], [0, 4, 5], [7, 8, 6]],
    [[1, 0, 2], [4, 5, 3], [7, 8, 6]],
    [[1, 3, 0], [4, 2, 5], [7, 8, 6]],
    [[4, 1, 3], [7, 2, 5], [0, 8, 6]],
    [[4, 1, 3], [0, 2, 5], [7, 8, 6]],
    [[1, 2, 3], [7, 4, 5], [0, 8, 6]],
    [[1, 8, 2], [0, 4, 3], [7, 6, 5]],
    [[1, 2, 3], [5, 0, 6], [4, 7, 8]],
    [[1, 3, 5], [4, 2, 0], [7, 8, 6]],
    [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
    [[1, 5, 2], [4, 0, 3], [7, 8, 6]],
    [[4, 1, 2], [7, 5, 3], [8, 0, 6]],
    [[7, 2, 4], [5, 0, 6], [8, 3, 1]],
    [[8, 6, 7], [2, 5, 4], [3, 0, 1]],
    [[6, 4, 7], [8, 5, 0], [3, 2, 1]],
    [[4, 5, 8], [1, 7, 6], [0, 3, 2]],
    [[2, 7, 5], [0, 8, 4], [3, 1, 6]],
    [[8, 3, 5], [4, 1, 6], [2, 7, 0]],
    [[5, 3, 6], [1, 4, 8], [0, 7, 2]],
    [[8, 1, 2], [0, 4, 3], [7, 6, 5]],
    [[3, 4, 8], [1, 2, 7], [6, 5, 0]],
    [[5, 6, 7], [4, 0, 8], [3, 2, 1]],
    [[1, 7, 2], [8, 0, 3], [6, 5, 4]],
    [[0, 7, 2], [4, 6, 1], [3, 5, 8]],
    [[3, 4, 8], [1, 2, 5], [7, 0, 6]],
    [[2, 1, 6], [4, 0, 8], [7, 5, 3]],
    [[1, 5, 7], [2, 8, 3], [4, 0, 6]],
]

def get_instance(i):
    s0 = Node()
    s0.map = TEST_MAPS[i]
    return s0