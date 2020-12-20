import os
from copy import deepcopy
from collections import defaultdict
from math import sqrt
import itertools

class Tile:
    def __init__(self, id, lines):
        self.id = id
        self.data = [[x for x in line] for line in lines]
        self.create_rotations()

    def match_border(self, orientation, side):
        data = self.rotations[orientation]
        if side == 0:
            return list(data[0])
        if side == 2:
            return list(data[-1])
        if side == 1:
            return [line[-1] for line in data]
        if side == 3:
            return [line[0] for line in data]

    def inside(self, orientation):
        data = self.rotations[orientation]
        return [list(line[1:-1]) for line in data[1:-1]]

    def create_rotations(self):
        self.rotations = []
        current = deepcopy(self.data)
        for _ in range(4):
            current = list(zip(*reversed(current)))
            self.rotations.append(deepcopy(current))
            self.rotations.append(deepcopy(current[::-1]))

with open("input.txt") as f:
    lines = f.read().splitlines()

    tiles = []
    i = 0
    while i < len(lines):
        id = int(lines[i][5:9])
        tiles.append(
            Tile(id, lines[i+1:i+11])
        )
        i = i + 12

neighbours = defaultdict(set)

for a in range(len(tiles)-1):
    for o_a in range(8):
        for side in range(4):
            border_a = tiles[a].match_border(o_a, side)
            for b in range(a+1,len(tiles)):
                for o_b in range(8):
                    border_b = tiles[b].match_border(o_b, (side + 2) % 4)
                    if border_a == border_b:
                        neighbours[(a, tiles[a].id)].add((b, tiles[b].id))
                        neighbours[(b, tiles[b].id)].add((a, tiles[a].id))

value = 1
for key, values in neighbours.items():
    if len(values) == 2:
        value = value * key[1]

print("Part 1: " + str(value))

with open("input.txt") as f:
    lines = f.read().splitlines()

    tiles = []
    i = 0
    while i < len(lines):
        id = int(lines[i][5:9])
        tiles.append(
            Tile(id, lines[i+1:i+11])
        )
        i = i + 12

matches = {}
neighbours = defaultdict(set)

for a in range(len(tiles)-1):
    for o_a in range(8):
        for side in range(4):
            border_a = tiles[a].match_border(o_a, side)
            for b in range(a+1,len(tiles)):
                for o_b in range(8):
                    border_b = tiles[b].match_border(o_b, (side + 2) % 4)
                    if border_a == border_b:
                        matches[(a, o_a, side)] = (b, o_b)
                        matches[(b, o_b, (side + 2) % 4)] = (a, o_a)
                        neighbours[a].add(b)
                        neighbours[b].add(a)

puzzle_size = int(sqrt(len(tiles)))
puzzle = [[None for _ in range(puzzle_size)] for _ in range(puzzle_size)]

top_edge = [
    id for id, values in neighbours.items() if len(values) == 2
]

corner = top_edge[0]
for orientation in range(8):
    if (corner, orientation, 1) in matches and (corner, orientation, 2) in matches:
        puzzle[0][0] = (corner, orientation)
        break

for x in range(puzzle_size - 1):
    for y in range(puzzle_size):
        if y < puzzle_size -1:
            puzzle[x][y + 1] = matches[puzzle[x][y] + (1,)]
        puzzle[x + 1][y] = matches[puzzle[x][y] + (2,)]

full_puzzle = [
    [tiles[puzzle[x][y][0]].inside(puzzle[x][y][1]) for y in range(puzzle_size)] for x in range(puzzle_size)
]

image = []
for x in range(puzzle_size):
    for x1 in range(8):
        line = []
        for y in range(puzzle_size):
            line.extend(full_puzzle[x][y][x1])
        image.append(line)

rotations = []
current = deepcopy(image)
for _ in range(4):
    current = [list(line) for line in zip(*reversed(current))]
    rotations.append(deepcopy(current))
    rotations.append(deepcopy(current[::-1]))

monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]
monster_h = len(monster)
monster_w = len(monster[0])
image_h = len(image)
image_w = len(image[0])

for image in rotations:
    monsters = 0
    for x in range(image_h - monster_h):
        for y in range(image_w - monster_w):
            monster_found = True
            for (x1, y1) in itertools.product(range(monster_h), range(monster_w)):
                if monster[x1][y1] == "#" and image[x + x1][y + y1] != "#":
                    monster_found = False
                    break

            if monster_found:
                monsters = monsters + 1
                for (x1, y1) in itertools.product(range(monster_h), range(monster_w)):
                    if monster[x1][y1] == "#":
                        image[x + x1][y + y1] = "O"

    if monsters > 0:
        print("Part 2: " + str(sum(line.count("#") for line in image)))