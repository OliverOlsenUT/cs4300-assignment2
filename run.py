import argparse
import sys

from astar import AStar
from helpers import print_solution_path, get_instance, h0, h1, h2

if __name__ == "__main__":
    p = argparse.ArgumentParser(prog="8-Puzzle Solver", 
                                description="Solves the 8-Puzzle with the chosen algorithm, displaying results.")
    p.add_argument("-hr", "--heuristic", help="The heuristic to use (h0, h1, h2).", type=str, required=False, default="h2")
    p.add_argument("-i", "--instance", help="The instance number to use (0-29)", type=int, default=0)

    parsed = p.parse_args(sys.argv[1::])
    inst = get_instance(parsed.instance)
    if parsed.heuristic.upper() == "H0":
        h = h0
    elif parsed.heuristic.upper() == "H1":
        h = h1
    else:
        h = h2
    d = AStar(h)
    p = d.main(inst)
    print(p)
    print_solution_path(inst, p.prev_actions)
