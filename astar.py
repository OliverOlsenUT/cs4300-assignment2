class AStar():
    def __init__(self):
        pass
    def pop_min(self):
        if not self.queue:
            return None
        

        
        # pops the queue with the least amount of cost TODO
        return self.queue.pop()
    def c(self, a, b, c):
        pass
    def g(self, a):
        pass
    def h(self, a):
        pass
    def main(self, s0):
        self.queue = []
        best_g = {}
        best_g[s0] = 0
        while self.queue:
            n = self.pop_min()
            if self.goal_test(n.state):
                return n#solution path from s0 to n_state TODO
            for a in n.actions():
                s_ = n.transition(a)
                g_ = self.g(n) + self.c(n.state, a, s_)
                if s_ not in best_g or g_ < best_g[s_]:
                    best_g[s_] = g_
                    self.push(s_, g_ + self.h(s_))