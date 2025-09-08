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

class UCS():
    def __init__(self):
        self.queue = []

    def pop_min(self):
        if not self.queue:
            return None
        
        min_node = min(self.queue, key=lambda node: node.g)
        self.queue.remove(min_node)
        return min_node

    def push(self, item, score):
        item.g = score
        self.queue.append(item)

    def main(self, s0):
        self.queue = [s0]
        best_g = {s0: 0}

        while self.queue:
            n = self.pop_min()

            if goal_test(n):
                return n

            for a in n.actions():
                s_ = n.transition(a)
                g_ = n.g + self.cost(n, a)
                if s_ not in best_g or g_ < best_g[s_]:
                    best_g[s_] = g_
                    self.push(s_, g_)
        return "fail"

    def cost(self, state, action):
        return 1
                
GOAL = Node()
def goal_test(n):
    return n == GOAL

def main():
    u = UCS()
    s0 = Node()
    s0.map = [[1,2,3],[4,5,6],[0,7,8]]
    n = u.main(s0)
    print(n.prev_actions)

if __name__ == "__main__":
    main()