import argparse
import sys

from astar import AStar
from helpers import get_instance, h0, h1, h2

if __name__ == "__main__":
    print("|Instance|Nodes Expanded|Nodes Generated|Max Frontier Size|Solution Depth|Solution Cost|")
    print("|--------|--------------|---------------|-----------------|--------------|-------------|")
    for i in range(30):
        inst = get_instance(i)
        for h in [h0,h1,h2]:
            d = AStar(h)
            p = d.main(inst)
            print(f"|{h.__name__} {i}|{p.nodes_expanded}|{p.nodes_generated}|{p.maximum_frontier_size}|{p.solution_depth}|{p.solution_cost}|")
