import json
from argparse import ArgumentParser
from src.game import LangtonsAnt

parser = ArgumentParser()
parser.add_argument("--file", help="initial grid", required=True)
parser.add_argument("--initial_x", type=int, help='initial x coordinate of the ant', required=True)
parser.add_argument("--initial_y", type=int, help='initial y coordinate of the ant', required=True)
parser.add_argument("--steps", type=int, help='number of steps to simulate', required=True)

args = parser.parse_args()

with open(args.file) as grid_file:
    grid = json.load(grid_file)
    game = LangtonsAnt(grid, (args.initial_x, args.initial_y))
    game.simulate(args.steps)
