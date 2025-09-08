from helpers import Node, goal_test

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

def main():
    u = UCS()
    s0 = Node()
    s0.map = [[1,2,3],[4,5,6],[0,7,8]]
    n = u.main(s0)
    print(n.prev_actions)

if __name__ == "__main__":
    main()