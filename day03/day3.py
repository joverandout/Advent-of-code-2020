map = []

def update(X, Y, x, y):
    X += x
    Y += y
    return X, Y

def fillmap():
    with open('input.txt') as file:
        for line in file:
            line = list(line.strip('\n'))
            map.append(line)

def path(map, changeX, changeY, x , y, count):
    while len(map) > y:
        if x >= len(map[0]):
            x -= len(map[0])
        if map[y][x] == "#":
            count += 1
        x, y = update(x, y, changeX, changeY)
    return count

fillmap()
print(path(map, 3, 1, 0, 0, 0))
print(path(map, 3, 1, 0, 0, 0)+path(map, 1, 1, 0, 0, 0)
    *path(map, 3, 1, 0, 0, 0)*path(map, 5, 1, 0, 0, 0)
    *path(map, 7, 1, 0, 0, 0)*path(map, 1, 2, 0, 0, 0))