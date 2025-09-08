import heapq
from helpers import *
import itertools

class AStar():
    def __init__(self, heuristic):
        self.goal_map = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.goal_positions = {tile: (r, c) for r, row in enumerate(self.goal_map) for c, tile in enumerate(row) if tile != 0}
        self.h = heuristic

    def heuristic(self, node):
        return self.h(node)

    def cost(self, node, action, next_node):
        return 1
        
    def main(self, s0):
        frontier = []
        s0.g = 0
        f0 = s0.g + self.heuristic(s0)
        
        tie_breaker = itertools.count()
        
        heapq.heappush(frontier, (f0, next(tie_breaker), s0))
        
        best_g = {s0: 0}
        
        while frontier:
            f, _, n = heapq.heappop(frontier)
            
            if goal_test(n):
                return n
            
            for a in n.actions():
                s_ = n.transition(a)
                g_ = n.g + self.cost(n, a, s_)
                
                if s_ not in best_g or g_ < best_g[s_]:
                    best_g[s_] = g_
                    s_.g = g_
                    f_ = g_ + self.heuristic(s_)
                    heapq.heappush(frontier, (f_, next(tie_breaker), s_))
        
        return None
    
def main():
    u = AStar(h2)
    s0 = Node()
    s0.map = [[1,2,3],[4,5,6],[0,7,8]]
    n = u.main(s0)
    print(n.prev_actions)

if __name__ == "__main__":
    main()