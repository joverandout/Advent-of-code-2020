import math
import itertools
import copy

def changeGrid(grid, grid2, count, i , j ,k):
    if (grid[i][j][k] == '#') and (not(2 <= count <= 3)):
        grid2[i][j][k] = '.'

    if (grid[i][j][k] == '.') and (count == 3):
        grid2[i][j][k] = '#'
    return grid2

def iterate6Times(grid):
    grid2 = copy.deepcopy(grid)
    for i in range(24):
        for j in range(24):
            for k in range(24):
                count = 0
                for z in itertools.product([0, 1, -1], repeat=3):
                    if((0 <= i + z[0] <= 23) and (0 <= k + z[2] <= 23) and (0 <= j + z[1] <= 23)):
                        if(grid[i+z[0]][j+z[1]][k+z[2]] == '#'):
                            if not(z == (0, 0, 0)):
                                count += 1
                grid2 = changeGrid(grid, grid2, count, i, j, k)
    return grid2
    

def part1(grid, data):
    for ix, i in enumerate(data):
        for jx, j in enumerate(i):
            grid[12][ix+9][jx+9] = j
    for _ in range(6):      
        grid = iterate6Times(grid)
    cells = 0
    for i in range(24):
        for j in range(24):
            for k in range(24):
                if grid[i][j][k] == '#':
                    cells += 1
    return cells

with open('input.txt') as file:
    input = [line
             for line in file.read().splitlines()]
    print(part1([[['.' for _ in range(24)] for _ in range(24)] for _ in range (24)], input))
