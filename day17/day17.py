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

def iterate4d(grid, grid2, rows, iterate, columns, si, sj, sk, sl, iterations):
    for i in range(1 + iterations):
            for j in range(1 + iterations):
                for k in range(rows + iterations):
                    for l in range(columns + iterations):
                        count = 0
                        for z in itertools.product([0, 1, -1], repeat=4):
                            if((0 <= i + si + z[0] < 1 + (iterate*2)) and (0 <= j + sj + z[1] < 1 + (iterate*2)) and (0 <= k + sk + z[2] < rows + (iterate*2))):
                                    if ((0 <= l + sl + z[3] < columns + (iterate*2)) and (grid[i + si + z[0]][j + sj + z[1]][k + sk + z[2]][l + sl + z[3]] == '#')):
                                        if not(z == (0, 0, 0, 0)):
                                            count += 1
                        if (grid[i + si][j + sj][k + sk][l + sl] == '#') and (not(2 <= count <= 3)):
                            grid2[i + si][j + sj][k + sk][l + sl] = '.'

                        if (grid[i + si][j + sj][k + sk][l + sl] == '.') and (count == 3):
                            grid2[i + si][j + sj][k + sk][l + sl] = '#'
    return grid2

def part2(grid, data, rows, columns, iterate):
    for ix, i in enumerate(data):
        for jx, j in enumerate(i):
            grid[iterate][iterate][ix + iterate][jx + iterate] = j

    si = sj = sk = sl = iterate - 1

    for loop in range(iterate):
        grid2 = copy.deepcopy(grid)
        grid = iterate4d(grid, grid2, rows, iterate, columns, si, sj, sk, sl, 2 *(loop+1))
        si, sj, sk, sl = si - 1, sj - 1, sk - 1, sl - 1

    active = 0
    for i in range(1 + (iterate*2)):
        for j in range(1 + (iterate*2)):
            for k in range(rows + (iterate*2)):
                for l in range(columns + (iterate*2)):
                    if grid[i][j][k][l] == '#':
                        active += 1
    return active
    
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
    print("Part 1: " + str(part1([[['.' for _ in range(24)] for _ in range(24)] for _ in range (24)], input)))
    print("Part 2: "  + str(part2([[[['.' for _ in range(len(input[0]) + 12)] for _ in range(len(input) + 12)] for _ in range(1 + 12)] for _ in range(1 + 12)], input, len(input), len(input[0]), 6)))
